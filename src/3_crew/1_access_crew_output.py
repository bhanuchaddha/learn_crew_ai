# Import required modules from crewai library and custom models
from crewai import Agent, Crew, Process, Task
from src.models import CustomerAndProductData


def main():
    # Create a data generator agent with specific role and responsibilities
    data_generator_agent = Agent(
        name="DataGeneratorAgent",
        role="Data Generator",
        goal="Generate data Customer and Product Data",
        description="Generate fake data  for Customer and Products",
        backstory="This agent is the first agent in the crew",
        verbose=True,
    )

    # Define a task for data generation with structured output using Pydantic model
    data_generator_task=Task(
            name="DataGenerationTask",
            description="Task to generate data for Customer and Products. Initialialy shopping cart of each customer is empty",
            expected_output="Fake Customer and Products data",
            agent=data_generator_agent,
            output_pydantic=CustomerAndProductData  # Ensures type-safe output handling
            )

    # Create a crew with the data generator agent and its task
    first_crew = Crew(
        agents=[data_generator_agent],
        name="FirstCrew",
        description="Crew to run tasks",
        tasks=[data_generator_task],
        verbose=True,  # Enable detailed logging
    )
    
    # Execute the crew's tasks and store the result
    result=first_crew.kickoff()
    
    # Demonstrate three different methods to access the crew's output:

    # Method 1: Dictionary-style access
    # Directly access properties using dictionary notation
    print("Option 1 - Accessing Properties - - direcly from result")
    customers = result["customers"]
    products = result["products"]
    print("Customers:", customers)
    print("Products:", products)

    # Method 2: Pydantic model access
    # Access properties through the Pydantic model interface
    print("Option 2: Accessing Properties Directly from the Pydantic Model")
    customers = result.pydantic.customers
    products = result.pydantic.products
    print("Customers using pydentic:", customers)
    print("Products using pydentic:", products)

    # Method 3: to_dict() method
    # Convert the result to a dictionary and access properties
    print("Option 3: Accessing Properties Using the to_dict() Method")
    output_dict = result.to_dict()
    customers = output_dict["customers"]
    products = output_dict["products"]
    print("Customers using to_dict():", customers)
    print("Products using to_dict():", products)

    # Method 4: Accessing properties using json_dict
    print("Option 4: Accessing Properties Using the json_dict")
    print("it only work if output_json=CustomerAndProductData")
    print("json dict", result.json_dict)

    # Method 5: Accessing properties using tasks_output
    # print("Task Output:", result.tasks_output)

if __name__ == "__main__":
    main()
