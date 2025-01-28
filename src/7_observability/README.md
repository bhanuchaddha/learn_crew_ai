Sign up for Langtrace

Sign up by visiting https://langtrace.ai/signup.

2
Create a project

Set the project type to CrewAI and generate an API key.

3
Install Langtrace in your CrewAI project

Use the following command:


pip install langtrace-python-sdk
4
Import Langtrace

Import and initialize Langtrace at the beginning of your script, before any CrewAI imports:


from langtrace_python_sdk import langtrace
langtrace.init(api_key='<LANGTRACE_API_KEY>')

# Now import CrewAI modules
from crewai import Agent, Task, Crew