import difflib

def evaluate_response(user_response: str, possible_answers: list) -> dict:
    """
    Evalúa la respuesta del usuario en función de las posibles respuestas.

    Args:
        user_response (str): Respuesta del usuario.
        possible_answers (list): Lista de respuestas esperadas.

    Returns:
        dict: Resultado con la respuesta más similar y el puntaje de similitud.
    """
    if not user_response or not possible_answers:
        return {"best_match": None, "score": 0.0}

    matches = difflib.get_close_matches(user_response, possible_answers, n=1, cutoff=0.6)
    
    best_match = matches[0] if matches else None
    score = difflib.SequenceMatcher(None, user_response, best_match).ratio() if best_match else 0.0

    return {"best_match": best_match, "score": score}
