from fastapi import FastAPI

from src.controllers import interviewer_controller  

app = FastAPI()


app.include_router(interviewer_controller.router, prefix="/api/interview", tags=["Interviewer"])
