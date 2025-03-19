from fastapi import APIRouter, HTTPException
from typing import Dict, Any

from ..services.interviewer_service import InterviewerService

router = APIRouter()
interviewer_service = InterviewerService()

@router.post("/interview")
async def interview(data: Dict[str, Any]):
    try:
        vacant = data.get("name")
        new_questions = data.get("questions")
        
        if not vacant or not new_questions:
            raise HTTPException(status_code=400, detail="Missing data")

        result = interviewer_service.conduct_interview(vacant, new_questions)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding questions: {str(e)}")
