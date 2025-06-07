from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str

class UserRead(UserCreate):
    id: int

    class Config:
        orm_mode = True
        
class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
