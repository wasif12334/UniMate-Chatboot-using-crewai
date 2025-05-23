from crewai.flow import Flow, listen, start, router
from unimatechatbot.crews.unimate_crew.unimate import Unimate
from pydantic import BaseModel
from typing import Literal

class QueryClassifier(BaseModel):
   Query: Literal["personal_info", "course_query", "appointment_request"]

class UnimateFlow(Flow[str]):

    @start
    def startup_function(self):
        print("StartupFunction Called")
        UI_Ins = Unimate.UI_Agent()
        query = UI_Ins.kickoff("I want to study DSA for Semester Exam Explain the important topics")
        return query

    @listen("startup_function")
    def classify_query(self, query):
        print("QueryClassifier Called")
        QC_Ins = Unimate.QueryClassifier_Agent(query)
        cl_query = QC_Ins.kickoff()
        return cl_query

    @router(QueryClassifier)
    def route_query(self, cl_query: str) -> str:
        print(f"📬 Routing query to: {cl_query}")
        if cl_query in ["course_query", "personal_info", "appointment_request"]:
            return cl_query
        else:
            return "fallback"

    @listen("course_query")
    def handle_course_query(self, cl_query):
        agent = Unimate.KnowledgeBase_Agent(cl_query)
        return agent.kickoff()

    @listen("personal_info")
    def handle_personal_info(self, cl_query):
        agent = Unimate.Personalized_Agent(cl_query)
        return agent.kickoff()

    @listen("appointment_request")
    def handle_booking(self, cl_query):
        agent = Unimate.Appointment_Agent(cl_query)
        return agent.kickoff()

    @listen("fallback")
    def handle_fallback(self, cl_query):
        agent = Unimate.Escalation_Agent(cl_query)
        return agent.kickoff()

def kickoff():
    Unimate_Flow = UnimateFlow()
    Unimate_Flow.kickoff()


def plot():
    Unimate_Flow = UnimateFlow()
    Unimate_Flow.plot()