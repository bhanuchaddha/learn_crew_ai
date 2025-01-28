# Import required modules from crewai library and custom models for structured data handling
from crewai import Agent, Crew, Process, Task
from src.models import CustomerAndProductData


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
            output_json=CustomerAndProductData  # Use JSON format for structured output
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
    
    # Demonstrate how to access the JSON-formatted output:

    # Method 1: Direct dictionary-style access
    # Access the JSON data using standard dictionary notation
    print("Option 1 - Accessing Properties directly from JSON result")
    customers = result["customers"]
    products = result["products"]
    print("Customers:", customers)
    print("Products:", products)

    # Display the complete JSON output
    print("Complete JSON output:")
    print(result)


if __name__ == "__main__":
    main()
