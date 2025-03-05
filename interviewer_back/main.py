from fastapi import FastAPI
from src.controllers import interviewer_controller  # Ajusta la ruta según tu estructura

app = FastAPI()

# Incluir el router del controlador
app.include_router(interviewer_controller.router, prefix="/api/interview", tags=["Interviewer"])
