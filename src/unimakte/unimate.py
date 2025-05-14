from crewai import Crew,process,task
from crewai.project import CrewBase,agent,crew,task
from dotenv import load_dotenv

load_dotenv()

@crew
class Unimate():
    agents_config='config/unimate/agents.yaml'
    task_config='config/unimate/task.yaml'

    @agent
    def Task_magner():
        return agent(
            config=agents_config,
            verbose=true,
            memory=true
        )
    
    @agent
    def study_assistant():
        return agent(
            config=agents_config,
            verbose=true,
            memory=true
        )
    
    @agent
    def note_organizer():
        return agent(
            config=agents_config,
            verbose=true,
            memory=true
        )
    
    @agent 
    def content_gernator():
        return agent(
            config=agents_config,
            verbose=true,
            memory=true
        )
