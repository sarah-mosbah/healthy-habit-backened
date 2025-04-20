from crewai import Agent
from langchain.chat_models import ChatOpenAI

def get_habit_coach():
    return Agent(
        role="Habit Coach",
        goal="Help users build healthy routines tailored to their preferences.",
        backstory="You are an expert in behavioral science and personal coaching.",
        llm=ChatOpenAI(model_name="gpt-4o", temperature=0.5),
    )
