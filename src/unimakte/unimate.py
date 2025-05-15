from crewai import Crew, Process, Agent,task
from crewai.project import CrewBase, agent, crew,task
from crewai.agents.agent_builder.base_agent import BaseAgent
from dotenv import load_dotenv
from typing import List

load_dotenv()

@CrewBase
class Unimate():
    """Unimakte crew"""

    agents: List[BaseAgent]
    tasks: List[task]

    @agent
    def TaskManager(self) -> Agent:
        return Agent(
            config=self.agents_config['manage_tasks'], 
            verbose=True
        )

    @agent
    def StudyAssistant(self) -> Agent:
        return Agent(
            config=self.agents_config['study_assistant'], 
            verbose=True
        )
    @agent
    def NoteOrganizer(self) -> Agent:
        return Agent(
            config=self.agents_config['note_organizer'], 
            verbose=True
        )
    @agent
    def ContentGenerator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_generator'], 
            verbose=True
        )

    
    @task
    def TaskManager_task(self) -> task:
        return task(
            config=self.tasks_config['manage_tasks'],
        )

    @task
    def StudyAssistant_task(self) -> task:
        return task(
            config=self.tasks_config['assist_study'],
            output_file='report.md'
        )
    @task
    def ContentGenerator_task(self) -> task:
        return task(
            config=self.tasks_config['create_content'],
            output_file='report.md'
        )
    @task
    def NoteOrganizer_task(self) -> task:
        return task(
            config=self.tasks_config['generate_notes'],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Unimakte crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )

def uni_mate():
    query="Want to khown about stufy plan for the DSA"
    result=Unimate().crew().kickoff(query)
    print(result)
