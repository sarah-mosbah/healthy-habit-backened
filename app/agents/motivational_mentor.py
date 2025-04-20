from crewai import Agent
from langchain.chat_models import ChatOpenAI

def get_motivational_mentor():
    return Agent(
        role="Motivates User To continue on his habits",
        goal= "Motivates user to be on track with his own habits by sending daily motivational quotes and focus tips",
        backstory="A calm, insightful voice for daily mental well-being.",
        llm= ChatOpenAI(model_name="gpt-4o", temperature=0.5)
    )
