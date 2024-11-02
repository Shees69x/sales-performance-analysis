from flask import Flask, request, jsonify
import pandas as pd
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
import os

app = Flask(__name__)
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Load and setup the sales data
def load_sales_data(file_path):
    if file_path.endswith('.csv'):
        return pd.read_csv(file_path)
    elif file_path.endswith('.json'):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format. Please use CSV or JSON.")

sales_data = load_sales_data("sales_performance_data.csv")

# Set up the LLM agent
def setup_agent(dataframe):
    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-3.5-turbo"),
        dataframe,
        verbose=True,
        allow_dangerous_code=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
    )
    return agent

agent = setup_agent(sales_data)

# 1. Individual Sales Representative Performance Analysis
@app.route('/api/rep_performance', methods=['GET'])
def rep_performance():
    rep_id = request.args.get("rep_id")
    if rep_id:
        try:
            response = agent.invoke(f"Provide a detailed performance analysis for sales rep {rep_id}.")
            return jsonify({"feedback": response})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Please provide a rep_id"}), 400

# 2. Overall Sales Team Performance Summary
@app.route('/api/team_performance', methods=['GET'])
def team_performance():
    try:
        response = agent.invoke("Provide a summary of the sales team’s overall performance.")
        return jsonify({"feedback": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# 3. Sales Performance Trends and Forecasting
@app.route('/api/performance_trends', methods=['GET'])
def performance_trends():
    time_period = request.args.get("time_period", "monthly")  # Default to monthly if not specified
    try:
        response = agent.invoke(f"Analyze sales data over the {time_period} period to identify trends and forecast future performance.")
        return jsonify({"feedback": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(debug=True)
