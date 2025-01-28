"""
This script demonstrates how to use different knowledge sources in CrewAI
to process and analyze data from various file formats.
"""

# Import required modules from crewai library
from crewai import Agent, Crew, Task
from crewai.knowledge.source.crew_docling_source import CrewDoclingSource
from crewai.knowledge.source.text_file_knowledge_source import TextFileKnowledgeSource
from crewai.knowledge.source.json_knowledge_source import JSONKnowledgeSource

def main():
    # Initialize different knowledge sources
    # 1. JSON source for structured data (customer information)
    json_source = JSONKnowledgeSource(
        file_paths=["customer.json"]
    )

    # 2. Text file source for simple text data (product information)
    txt_source = TextFileKnowledgeSource(
        file_paths=["products.txt"]
    )

    # 3. Docling source for complex file formats (transaction records)
    # Supports: PDF, DOCX, PPTX, XLSX, Images, HTML, AsciiDoc & Markdown
    docling_source = CrewDoclingSource(
        file_paths=["transactions.xlsx"]
    )

    # Create an agent specialized in knowledge gathering
    # This agent can access all three knowledge sources
    knowledge_gathering_agent = Agent(
        name="KnowledgeGatheringAgent",
        role="Knowledge Gatherer",
        goal="Gather knowledge about customers and products",
        description="Gather data for Customer and Products",
        backstory="You are expert in gathering data",
        knowledge_sources=[json_source, txt_source, docling_source],
        verbose=True,
    )

    # Define the task for answering questions based on gathered knowledge
    answer_questions_task = Task(
        name="AnswerQuestionsTask",
        description="Answer the question using knowledge gathered {user_question}",
        expected_output="Answers to the questions",
        agent=knowledge_gathering_agent
    )

    # Create a crew to manage the knowledge gathering process
    knowledge_crew = Crew(
        agents=[knowledge_gathering_agent],
        name="KnowledgeCrew",
        description="Crew to gather knowledge",
        tasks=[answer_questions_task],
        verbose=True,
    )
    
    # Execute different queries to demonstrate knowledge gathering capabilities
    questions = [
        "How many customers are there?",
        "How many products are there?",
        "How many products each customer bought, and what was the total cost for each customer?"
    ]
    
    # Process each question
    for question in questions:
        knowledge_crew.kickoff({"user_question": question})

if __name__ == "__main__":
    main()
