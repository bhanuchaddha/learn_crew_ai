from crewai import LLM, Agent, Crew, Process, Task

llm = LLM(
    model="anthropic/claude-3-5-sonnet-latest",
    temperature=0.7
)

def main():
    first_agent = Agent(
        name="FirstAgent",
        role="Greeter",
        goal="Greet the user",
        description="This is the first agent",
        backstory="This agent is the first agent in the crew",
        llm=llm,
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
        llm=llm,
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
