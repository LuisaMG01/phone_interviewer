from src.services.interviewer_service import InterviewerService

questions = {
    "name": "Desarrollador de Software",
    "questions": [
        {
            "id": 1,
            "titleQuestion": "¿Cuál es tu experiencia con Python?",
            "possibleAnswers": ["Principiante", "Intermedio", "Avanzado"]
        },
        {
            "id": 2,
            "titleQuestion": "¿Has trabajado con frameworks web?",
            "possibleAnswers": ["Sí", "No"]
        }
    ]
}

def main():
    interviewer = InterviewerService()
    results = interviewer.conduct_interview(questions)
    
    print("\n📊 Resultados de la entrevista:")
    print(results)

if __name__ == "__main__":
    main()


