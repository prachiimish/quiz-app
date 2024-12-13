from django.shortcuts import render, redirect
from .models import Question

def quiz(request):
    if request.method == "POST":
        # Process submitted answers
        user_score = {"correct": 0, "incorrect": 0}
        
        # Iterate over all questions to check answers
        for question in Question.objects.all():
            selected_answer = request.POST.get(f"choice_{question.id}")  # Get the submitted answer for this question
            if selected_answer == question.correct_choice:  # Compare with the correct answer
                user_score["correct"] += 1
            else:
                user_score["incorrect"] += 1

        # Pass score to the result template
        return render(request, "quiz/result.html", {"score": user_score})

    # For GET requests, retrieve all questions to display
    questions = Question.objects.all()
    print(questions)
    return render(request, "quiz/index.html", {"questions": questions})
