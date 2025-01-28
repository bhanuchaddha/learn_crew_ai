# Import required modules from crewai library and custom models
from crewai import Agent, Crew, Process, Task
from src.models import CustomerAndProductData


def main():
    # Create the first agent responsible for generating customer and product data
    data_generator_agent = Agent(
        name="DataGeneratorAgent",
        role="Data Generator",
        goal="Generate data Customer and Product Data",
        description="Generate fake data  for Customer and Products",
        backstory="This agent is the first agent in the crew",
        verbose=True,
    )
    # Define the task for data generation with Pydantic model for structured output
    data_generator_task=Task(
            name="DataGenerationTask",
            description="Task to generate data for Customer and Products. Initialialy shopping cart of each customer is empty",
            expected_output="Fake Customer and Products data",
            agent=data_generator_agent,
            output_pydantic=CustomerAndProductData  # Use Pydantic model for type-safe output
            )

    # Create the second agent that will process the output from the first agent
    second_agent = Agent(
        name="SecondAgent",
        role="Replier",
        goal="Reply to the user",
        description="This is the second agent",
        backstory="This agent is the second agent in the crew",
        verbose=True,
    )

    # Define the second task with dependency on the first task
    second_task=Task(
            name="ReplyTask",
            description="Task to reply to the user",
            expected_output="Any reply to the greeting in the same language as Greting from previous Agent!",
            dependencies=[data_generator_task],  # This task depends on completion of data_generator_task
            agent=second_agent,
            )
    
    # Create a crew with both agents and their respective tasks
    first_crew = Crew(
        agents=[data_generator_agent, second_agent],
        name="HelloCrew",
        description="Crew to greet and reply to the user",
        tasks=[data_generator_task, second_task],
        verbose=True,
    )
    
    # Execute the crew's tasks and get the overall output
    crew_output=first_crew.kickoff()
    print(f"Crew Output:{crew_output}")

    # Access the output specifically from the data generation task
    data_generator_task_output = data_generator_task.output

    # Print various forms of the task output for analysis
    print(f"First task Output:{data_generator_task_output}")
    print(data_generator_task_output)
    print(f"Task Description: {data_generator_task_output.description}")
    print(f"Task Summary: {data_generator_task_output.summary}")
    print(f"Raw Output: {data_generator_task_output.raw}")
    
    # Print JSON output if available
    if data_generator_task_output.json_dict:
        print(f"JSON Output: {json.dumps(data_generator_task_output.json_dict, indent=2)}")
    
    # Print Pydantic model output if available
    if data_generator_task_output.pydantic:
        print(f"Pydantic Output: {data_generator_task_output.pydantic}")

if __name__ == "__main__":
    main()
