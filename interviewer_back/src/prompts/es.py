AI_QUESTION_PROMPT = (
    """
    Dado que estamos entrevistando a un candidato para el puesto de {vacant}, haz la pregunta {question}. 
    Haz que suene natural, necesito que seas conciso en la pregunta, como si un entrevistador humano la estuviera haciendo.
    """
)

USER_ANSWER_PROMPT = (
    """
    El candidato ha respondido: "{user_choice}". 
    Las opciones de respuesta posibles son: {possibleAnswers}. 

    Necesito que me digas de la respuesta del usuario  cual hace referencia de la lista de posibles respuestas, asi que el nombre de la posible respuesta a
    la que se refería el usuario es, devuelveme solo el valor de {possibleAnswers} al que hace referencia: 

    """
)