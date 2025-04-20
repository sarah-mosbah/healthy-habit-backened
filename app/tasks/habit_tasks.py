from crewai import Task


def create_habit_plan_task(agent, goal, preferences):
    return Task(
        description=f"The user wants to achieve the goal: '{goal}' with preferences: '{preferences}'. Suggest a 7-day personalized healthy habit plan.",
        expected_output="A 7-day habit plan with actionable steps.",
        agent=agent,
    )
