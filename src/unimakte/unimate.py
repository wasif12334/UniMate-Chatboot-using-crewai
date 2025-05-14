from crewai import Crew,Process,task ,agent
from crewai.project import CrewBase,agent,crew ,task
from dotenv import load_dotenv
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

load_dotenv()

@CrewBase
class Unimate():
    # agents_config='config/agents.yaml'
    # task_config='config/task.yaml'

    agent:list[BaseAgent]
    task:list[task]
    @agent
    def task_manager(self):
        pass
    
    @agent
    def study_assistant(self):
        pass
    
    @agent
    def note_organizer(self):
      pass
    
    @agent 
    def content_generator(self):
      pass
    
    @crew
    def crew(self)->Crew:
       return Crew(
          agents=self.agents,
          tasks=self.tasks,
          process=Process.sequential,
          verbose=True
       )
    
def uni_mate():
    result= Unimate().crew().kickoff()   
    print(result)
