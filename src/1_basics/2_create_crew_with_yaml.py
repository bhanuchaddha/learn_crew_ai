# Import required modules from crewai library and custom models
from crewai import Agent, Crew, Process, Task
from crewai_tools import ScrapeWebsiteTool
import yaml


# Define file paths for YAML configurations
files = {
    'agents': 'src/1_basics/config/agents.yaml',
    'tasks': 'src/1_basics/config/tasks.yaml'
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)
print(configs)

# Assign loaded configurations to specific variables
agents_config = configs['agents']
tasks_config = configs['tasks']
print(agents_config['first_agent'])

def main():
    first_agent = Agent(config=agents_config['first_agent'] )
    greet_task=Task(config=tasks_config['greet_task'],
                    agent=first_agent)
            
    second_agent = Agent(config=agents_config['second_agent'])

    reply_task=Task(config=tasks_config['reply_task'],agent=second_agent)

    first_crew = Crew(
        agents=[first_agent, second_agent],
        name="HelloCrew",
        description="Crew to greet and reply to the user",
        tasks=[greet_task, reply_task],
        verbose=True,
    )
    
    input_data = {
        "greeter_country": "Japan",
        "replier_country": "France",
        "topic": "Technology Innovation",
        "year": "2023",
        "max_sentences": 3
    
}
    
    first_crew.kickoff(inputs=input_data)


if __name__ == "__main__":
    main()
