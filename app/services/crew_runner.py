from crewai import Crew, Process
from app.agents.habit_coach import get_habit_coach
from app.agents.motivational_mentor import get_motivational_mentor
from app.tasks.habit_tasks import create_habit_plan_task
from app.tasks.motivational_tasks import create_motivational_task
from app.services.db import user_profiles

async def run_habit_coach(goal: str, preferences: str, user_id):
    existing = await user_profiles.find_one({"user_id": user_id})
    if not existing:
        await user_profiles.insert_one({"user_id": user_id, "goal": goal, "preferences": preferences})
    agent = get_habit_coach()
    task = create_habit_plan_task(agent, goal, preferences)
    crew = Crew(
        agents=[agent],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )
    response = crew.kickoff()
   
    return {"plan": response}

async def run_motivation(user_id: str):
    agent = get_motivational_mentor()
    task = await create_motivational_task(agent, user_id)
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential)
    response = crew.kickoff()
    
    return {"plan": response}
   
