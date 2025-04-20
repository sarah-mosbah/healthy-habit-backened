from fastapi import APIRouter
from app.models.request_models import HabitRequest, UserQuery
from app.services.crew_runner import run_habit_coach, run_motivation


router = APIRouter()

@router.post("/generate-plan")
async def generate_plan(request: HabitRequest):
    print(request)  # Debug print
    return await run_habit_coach(request.goal, request.preferences, request.user_id)


@router.post("/daily-message")
async def daily_message(data: UserQuery):
    return await run_motivation(data.user_id)