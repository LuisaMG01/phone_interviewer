from typing import Dict, Any, List
from ..config import get_llm_connection
from .response_generator import get_user_response
from .response_evaluator import evaluate_response
from ..prompts import AI_QUESTION_PROMPT
from langchain_core.messages import HumanMessage

class InterviewerService:
    def __init__(self):
        self.llm = get_llm_connection()
        self.answered_questions = set()

    def _get_ai_question(self, question: Dict[str, Any], vacant: str) -> str:
        message = AI_QUESTION_PROMPT.format(question=question, vacant=vacant)
        try:
            llm_response = self.llm.invoke([HumanMessage(content=message)])
            return llm_response.content.strip() if llm_response else question
        except Exception as e:
            print(f"Error con LLM: {e}")
            return question

    def conduct_interview(self, vacant, questions: Dict[str, Any]) -> list:
        vacant = vacant
        results = []
        
        print(f"\nIniciando entrevista para la vacante: {vacant}\n")
        
        remaining_questions =  []
        for q in questions:
            remaining_questions.append(q['titleQuestion'])

        print(remaining_questions)
        while remaining_questions:
            current_question = remaining_questions[0]
            print(current_question)
            ai_question = self._get_ai_question(current_question, vacant)
            print(f"\n📝 {ai_question}")

            user_response = get_user_response(current_question)
            evaluation = evaluate_response(user_response, current_question.get("possibleAnswers", []))
            
            results.append({
                "question_id": current_question["id"],
                "user_response": user_response,
                "evaluation": evaluation
            })
            
            self.answered_questions.add(current_question["id"])
            remaining_questions.pop(0)
        
        return results