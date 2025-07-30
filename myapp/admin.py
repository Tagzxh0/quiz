from django.contrib import admin
from .models import Question, QuizResult, Profile

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'topic', 'correct_option')
    search_fields = ('question_text',)
    list_filter = ('topic',)

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'topic', 'score', 'total_questions', 'submitted_at')
    search_fields = ('user__username', 'topic')
    list_filter = ('topic', 'submitted_at')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_teacher')
    list_filter = ('is_teacher',)
