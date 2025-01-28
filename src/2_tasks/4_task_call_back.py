# Import required modules from crewai library and custom models for structured data handling
from crewai import Agent, Crew, Process, Task
from src.models import CustomerAndProductData


def callback_function(output):
    # Do something after the task is completed
    # Example: Send an email to the manager
    print(f"""
        Task completed!
        Task: {output.description}
        Output: {output.raw}
    """)

def main():
    # Create a specialized agent for generating customer and product data
    # This agent is configured with specific attributes to ensure focused data generation
    data_generator_agent = Agent(
        name="DataGeneratorAgent",
        role="Data Generator",
        goal="Generate data Customer and Product Data",
        description="Generate fake data  for Customer and Products",
        backstory="This agent is the first agent in the crew",
        verbose=True,  # Enable detailed logging of agent's actions
    )

    # Configure a task that uses JSON output format for structured data handling
    # The CustomerAndProductData model ensures type-safe JSON output
    data_generator_task=Task(
            name="DataGenerationTask",
            description="Task to generate data for Customer and Products. Initialialy shopping cart of each customer is empty",
            expected_output="Fake Customer and Products data",
            agent=data_generator_agent,
            output_json=CustomerAndProductData,  # Use JSON format for structured output
            callback=callback_function
            )

    # Initialize a crew with the data generator agent
    # This crew will manage the execution of the data generation task
    first_crew = Crew(
        agents=[data_generator_agent],
        name="FirstCrew",
        description="Crew to run tasks",
        tasks=[data_generator_task],
        verbose=True,  # Enable detailed logging of crew operations
    )
    
    # Execute the crew's task and capture the JSON-formatted result
    result=first_crew.kickoff()
    


if __name__ == "__main__":
    main()
