import difflib

def evaluate_response(user_response: str, possible_answers: list) -> dict:
    if not user_response or not possible_answers:
        return {"best_match": None, "score": 0.0}

    matches = difflib.get_close_matches(user_response, possible_answers, n=1, cutoff=0.6)
    
    best_match = matches[0] if matches else None
    score = difflib.SequenceMatcher(None, user_response, best_match).ratio() if best_match else 0.0

    return {"best_match": best_match, "score": score}