from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from typing import Dict, Any, List
from config import load_config
from ..prompts import AI_QUESTION_PROMPT, USER_ANSWER_PROMPT
import difflib

config = load_config()

class InterviewerService:
    def __init__(self):
        self.api_key = config["OPENROUTER_API_KEY"]
        self.base_url = config["BASE_URL"]
        self.model = config["MODEL_NAME"]
        self.llm = self._connect()
        self.answered_questions = set()

    def _connect(self) -> ChatOpenAI:
        return ChatOpenAI(
            model_name=self.model,
            base_url=self.base_url,
            api_key=self.api_key,
            temperature=0.7
        )

    def _get_ai_question(self, question: Dict[str, Any], vacant: str) -> str:
        message = AI_QUESTION_PROMPT.format(question=question['titleQuestion'], vacant=vacant)
        try:
            llm_response = self.llm.invoke([HumanMessage(content=message)])
            return llm_response.content.strip() if llm_response else question['titleQuestion']
        except Exception as e:
            print(f"❌ Error con LLM: {e}")
            return question['titleQuestion']

    def _check_other_questions(self, user_answer: str, questions: List[Dict[str, Any]]) -> List[Dict[str, str]]:
        """ Verifica si la respuesta del usuario también responde otra pregunta """
        matched_questions = []
        return matched_questions

    def _get_user_answer(self, question: Dict[str, Any]) -> List[Dict[str, str]]:
        user_answer = input("💬 Tu respuesta: ")
        for k in question:
            print(k)
        answers = question["possibleAnswers"]
        print(answers)
        message = USER_ANSWER_PROMPT.format(
            user_choice=user_answer,
            possibleAnswers=answers
        )
        llm_response = ""
        try:
            llm_response = self.llm.invoke([HumanMessage(content = message)])
            print(llm_response)
        except Exception as e:
            return
        return llm_response.content.strip()

    def conduct_interview(self, questions: Dict[str, Any]) -> list:
        vacant = questions["name"]
        results = []
        
        print(f"\n🎤 Iniciando entrevista para la vacante: {vacant}\n")
        
        remaining_questions = [q for q in questions["questions"] if q["id"] not in self.answered_questions]
        
        while remaining_questions:
           
            current_question = remaining_questions[0]
            print(current_question)

            # Mostrar la pregunta al usuario
            ai_question = self._get_ai_question(current_question, vacant)
            print(f"\n📝 {ai_question}")
            
            # Obtener la respuesta del usuario
            user_answers = self._get_user_answer(current_question)
            
            if user_answers:
                results.append((current_question["id"], user_answers))
                self.answered_questions.add(current_question["id"])
                remaining_questions.pop(0)
                
            
            remaining_questions = [q for q in questions["questions"] if q["id"] not in self.answered_questions]
        
        return results

def main(questions):
    interviewer = InterviewerService()
    results = interviewer.conduct_interview(questions)
    
    print("\n📊 Resultados de la entrevista:")
    print(results)

if __name__ == "__main__":
    main()