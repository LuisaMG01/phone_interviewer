from langchain_core.messages import HumanMessage
from ..config import get_llm_connection
from ..prompts import USER_ANSWER_PROMPT

def get_user_response(question: dict) -> str:
    llm = get_llm_connection()
    user_answer = input("💬 Tu respuesta: ")

    message = USER_ANSWER_PROMPT.format(
        user_choice=user_answer,
        possibleAnswers=question.get("possibleAnswers", [])
    )

    try:
        llm_response = llm.invoke([HumanMessage(content=message)])
        return llm_response.content.strip() if llm_response else ""
    except Exception as e:
        print(f"❌ Error al generar respuesta: {e}")
        return ""
