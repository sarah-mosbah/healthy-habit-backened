from crewai import Task
from app.services.db import user_profiles

async def create_motivational_task(agent, user_id):
    user_profile = await user_profiles.find_one({"user_id": user_id})
    
    goal = user_profile.get("goal", "their personal goal") if user_profile else "their personal goal"

    return Task(
        description=f"Send a motivational message to user {user_id} for today's habit journey. Their goal is: {goal}.",
        expected_output="A short, uplifting message based on their goal.",
        agent=agent
    )



