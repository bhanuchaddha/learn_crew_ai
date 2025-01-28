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

    # To enable scrapping any website it finds during it's execution
    scrapeWebsiteTool = ScrapeWebsiteTool()
    
    # Create a data generator agent with specific role and responsibilities
    webpage_info_agent = Agent(
        name="WebpageInfoAgent",
        role="Webpage Info",
        goal="Get information from a given webpage ",
        description="Get information from a webpage",
        backstory="This agent is the first agent in the crew",
        verbose=True,
    )
    webpage_info_task=Task(
        name="WebpageInfoTask",
        description="Task to get information from  {webpage_url}",
        agent=webpage_info_agent,
        expected_output="Web page Info",
        tools=[scrapeWebsiteTool]
    )
    

    # Create a crew with the data generator agent and its task
    first_crew = Crew(
        agents=[webpage_info_agent],
        name="FirstCrew",
        description="Crew to run tasks",
        tasks=[webpage_info_task],
        verbose=True,  # Enable detailed logging
    )
    
    # Execute the crew's tasks and store the result
    result=first_crew.kickoff({"webpage_url":"https://en.wikipedia.org/wiki/Donald_Trump"})
    
    # Demonstrate three different methods to access the crew's output:


    # Json output
    print("Result:")
    print(result)


if __name__ == "__main__":
    main()
