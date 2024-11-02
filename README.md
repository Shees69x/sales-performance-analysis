# sales-performance-analysis
Develop a backend system that uses a Large Language Model (LLM) to analyze sales data and provide feedback on both individual sales representatives and overall team performance.

## Technologies Used
- **Python**: Programming language for backend development.
- **Flask**: Web framework to build the RESTful APIs.
- **Pandas**: Data manipulation and analysis.
- **Langchain**: Framework for using language models.
- **OpenAI API**: To access the LLM.
- **Postman**: For testing the API endpoints.

## Setup and Run Instructions
1. Clone the repository

2. Set up a virtual environment:
   Activate the virtual environment
   python -m venv virenv

   Windows
   virenv\Scripts\activate
   
   macOS/Linux
   source virenv/bin/activate

4. Install the required packages:
   pip install -r requirements.txt

5. Set your OpenAI API key in the code or as an environment variable:
   export OPENAI_API_KEY='your_openai_api_key'  # Linux/macOS
   set OPENAI_API_KEY='your_openai_api_key'     # Windows
   $env:OPENAI_API_KEY = "your_openai_api_key"  # Powershell

7. Run the Flask application:
   python Analysis_app.py

## Testing
Testing Each API Endpoint
1. Individual Sales Representative Performance Analysis
Method: GET
Endpoint: http://127.0.0.1:5000/api/rep_performance
Parameters:
Key = rep_id (e.g Value = 183)
Steps:

In Postman, create a new request.
Set the method to GET.
Enter the URL: http://127.0.0.1:5000/api/rep_performance?rep_id=183
Click on the Send button.
Observe the response in the lower section of Postman.
2. Overall Sales Team Performance Summary
Method: GET
Endpoint: http://127.0.0.1:5000/api/team_performance
Steps:

Create another request in Postman.
Set the method to GET.
Enter the URL: http://127.0.0.1:5000/api/team_performance
Click on the Send button.
Check the response for the team's performance summary.
3. Sales Performance Trends and Forecasting
Method: GET
Endpoint: http://127.0.0.1:5000/api/performance_trends
Parameters:
Key = time_period (e.g. Value = monthly)
Steps:

Create another request in Postman.
Set the method to GET.
Enter the URL: http://127.0.0.1:5000/api/performance_trends?time_period=monthly
Click on the Send button.
Review the response for trends and forecasting analysis.
