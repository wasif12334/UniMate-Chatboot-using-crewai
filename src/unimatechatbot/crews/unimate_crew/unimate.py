#import the nesseassary libary first
from crewai import Crew,Process,Task,Agent
from crewai.project import CrewBase,task,agent,crew
from dotenv import load_dotenv
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

#load the model and api key from .env file
load_dotenv()

@CrewBase
class Unimate():

    agents:list[BaseAgent]
    tasks:list[Task]

    agents_config="config/agent.yaml"
    tasks_config="config/task.yaml"
    #Agent no 1
    @agent
    def UI_Agent(self) -> Agent :
        return Agent(
            config=self.config["UI_Agent"]
        )
    
    #Agent no 2
    @agent
    def QueryClassifier_Agent(self) -> Agent :
        return Agent(
            config=self.config["QueryClassifier_Agent"]
        )
    #Agent no 3
    @agent
    def KnowledgeBase_Agent(self) -> Agent :
        return Agent(
            config=self.config["KnowledgeBase_Agent"]
        )
    #Agent no 4
    @agent
    def Personalized_Agent(self) -> Agent :
        return Agent(
            config=self.config["Personalized_Agent"]
        )
    #Agent no 5
    @agent
    def Appointment_Agent(self) -> Agent :
        return Agent(
            config=self.config["Appointment_Agent"]
        )
    #Agent no 6
    @agent
    def Notification_Agent(self) -> Agent :
        return Agent(
            config=self.config["Notification_Agent"]
        )
    #Agent no 7
    @agent
    def Escalation_Agent(self) -> Agent :
        return Agent(
            config=self.config["Escalation_Agent"]
        )
    

                    ##-------------------##

    #Task-1
    @task
    def UserInteraction(self)->Task:
        return Task(
            config=self.config["UserInteraction"]
        )
    #Task-2
    @task
    def QueryClassifier(self)->Task:
        return Task(
            config=self.config["QueryClassifier"]
        )
    #Task-3
    @task
    def knowledgeRetrival(self)->Task:
        return Task(
            config=self.config["knowledgeRetrival"]
        )
    #Task-4
    @task
    def personalization(self)->Task:
        return Task(
            config=self.config["personalization"]
        )
    #Task-5
    @task
    def appointment_request(self)->Task:
        return Task(
            config=self.config["appointment_request"]
        )
    #Task-6
    @task
    def Notify(self)->Task:
        return Task(
            config=self.config["Notify"]
        )
    #Task-7
    @task
    def CallFor_HI(self)->Task:
        return Task(
            config=self.config["CallFor_HI"]
        )
    
    #crew
    @crew
    def crew(self)->Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
    

    



