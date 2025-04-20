from pydantic import BaseModel

class HabitRequest(BaseModel):
    goal: str
    preferences: str
    user_id: str

class UserQuery(BaseModel):
    user_id: str