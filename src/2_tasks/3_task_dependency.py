# Import required modules from crewai library and custom models for structured data handling
from crewai import Agent, Crew, Process, Task
from src.models import CustomerAndProductData, Customers, Products


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
    customer_data_generator_task=Task(
            name="CustomerDataGenerationTask",
            description="Task to generate data for 3 Customer. Initialialy shopping cart of each customer is empty",
            expected_output="Fake Customer data",
            agent=data_generator_agent,
            output_pydantic=Customers, # Use JSON format for structured output
            async_execution=True # Will be executed asynchronously
            )

    product_data_generator_task=Task(
            name="ProductDataGenerationTask",
            description="Task to generate 5 products",
            expected_output="Fake Product data",
            agent=data_generator_agent,
            output_pydantic=Products, # Use JSON format for structured output
            async_execution=True # Will be executed asynchronously
            )

    consolidate_generated_data_task=Task(
            name="ConsolidateGeneratedDataTask",
            description="Task to consolidate the generated data",
            expected_output="Consolidated data",
            agent=data_generator_agent,
            output_pydantic=CustomerAndProductData, # Use JSON format for structured output
            context=[customer_data_generator_task, product_data_generator_task]
            )

    # Initialize a crew with the data generator agent
    # This crew will manage the execution of the data generation task
    first_crew = Crew(
        agents=[data_generator_agent],
        name="FirstCrew",
        description="Crew to run tasks",
        tasks=[customer_data_generator_task, product_data_generator_task, consolidate_generated_data_task],
        verbose=True,  # Enable detailed logging of crew operations
    )
    
    # Execute the crew's task and capture the JSON-formatted result
    result=first_crew.kickoff()
    

    print(result)


if __name__ == "__main__":
    main()
