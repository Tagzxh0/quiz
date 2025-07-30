from django import forms
from .models import Question

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')  # Expecting a queryset of Question objects
        super().__init__(*args, **kwargs)

        for question in questions:
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=question.question_text,
                choices=[
                    ('option1', question.option1),
                    ('option2', question.option2),
                    ('option3', question.option3),
                    ('option4', question.option4),
                ],
                widget=forms.RadioSelect,
                required=False  # Set to False to allow skipped questions
            )
