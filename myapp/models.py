from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    TOPIC_CHOICES = [
        ('database_management', 'Database Management'),
        ('system_analysis', 'System Analysis and Design'),
        ('artificial_intelligence', 'Artificial Intelligence'),
        ('technopreneurship', 'Technopreneurship'),
        ('compiler_design', 'Compiler Design and Construction'),
    ]

    topic = models.CharField(
        max_length=50,
        choices=TOPIC_CHOICES,
        verbose_name="Topic"
    )
    question_text = models.TextField(verbose_name="Question Text")
    option1 = models.CharField(max_length=200, verbose_name="Option 1")
    option2 = models.CharField(max_length=200, verbose_name="Option 2")
    option3 = models.CharField(max_length=200, verbose_name="Option 3")
    option4 = models.CharField(max_length=200, verbose_name="Option 4")

    OPTION_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
    ]
    correct_option = models.CharField(
        max_length=10,
        choices=OPTION_CHOICES,
        verbose_name="Correct Option"
    )

    def __str__(self):
        return f"{self.get_topic_display()}: {self.question_text[:50]}..."

    def get_correct_answer_text(self):
        return getattr(self, self.correct_option)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_teacher = models.BooleanField(default=False)


class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=50, choices=Question.TOPIC_CHOICES)
    score = models.IntegerField()
    total_questions = models.IntegerField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.get_topic_display()} - {self.score}/{self.total_questions}"
