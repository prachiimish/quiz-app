from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=255)  # The question text
    option1 = models.CharField(max_length=255)  # First option
    option2 = models.CharField(max_length=255)  # Second option
    option3 = models.CharField(max_length=255)  # Third option
    option4 = models.CharField(max_length=255)  # Fourth option
    correct_choice = models.CharField(max_length=255)  # The correct answer

    def __str__(self):
        return self.question  # This will help easily identify questions in the admin panel

