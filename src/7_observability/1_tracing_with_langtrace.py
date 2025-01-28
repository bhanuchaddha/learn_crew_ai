from langtrace_python_sdk import langtrace
langtrace.init(api_key='<LANGTRACE_API_KEY>')



# Import required modules from crewai library and custom models
from crewai import Agent, Crew, Process, Task
from crewai_tools import ScrapeWebsiteTool



# # Initialize the tool with the website URL, 
# # so the agent can only scrap the content of the specified website
# tool = ScrapeWebsiteTool(website_url='https://www.example.com')

# # Extract the text from the site
# text = tool.run()
# print(text)




def main():
    first_agent = Agent(
        name="FirstAgent",
        role="Greeter",
        goal="Greet the user",
        description="This is the first agent",
        backstory="This agent is the first agent in the crew",
        verbose=True,
    )
    first_task=Task(
            name="GreetTask",
            description="Task to greet the user",
            expected_output="Any greeting in any language!",
            agent=first_agent,
            )




    second_agent = Agent(
        name="SecondAgent",
        role="Replier",
        goal="Reply to the user",
        description="This is the second agent",
        backstory="This agent is the second agent in the crew",
        verbose=True,
    )

    second_task=Task(
            name="ReplyTask",
            description="Task to reply to the user",
            expected_output="Any reply to the greeting in the same language as Greting from previous Agent!",
            dependencies=[first_task],
            agent=second_agent,
            )
    
    first_crew = Crew(
        agents=[first_agent, second_agent],
        name="HelloCrew",
        description="Crew to greet and reply to the user",
        tasks=[first_task, second_task],
        verbose=True,
    )
    
    first_crew.kickoff()


if __name__ == "__main__":
    main()
