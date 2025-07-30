from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden

from .models import Question, Profile, QuizResult
from .forms import QuizForm

# Student registration view
def register_student(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, is_teacher=False)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register_student.html', {'form': form})

# Redirect users based on login status
def root_redirect(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('public_home')

# Home view for logged-in users
@login_required
def home_view(request):
    return render(request, 'home.html')

# Public home view for visitors
def public_home_view(request):
    return render(request, 'public_home.html')

# Quiz page by topic
@login_required
def quiz_topic_view(request, topic):
    questions = Question.objects.filter(topic=topic)
    if not questions.exists():
        return render(request, 'no_questions.html', {'topic': topic})

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            results = []  # List to store question-by-question feedback

            for q in questions:
                selected = form.cleaned_data.get(f'question_{q.id}')
                is_correct = (selected == q.correct_option)
                if is_correct:
                    score += 1

                results.append({
                    'question': q,
                    'selected': selected,
                    'correct': q.correct_option,
                    'is_correct': is_correct,
                    'selected_text': getattr(q, selected) if selected else None,
                    'correct_text': getattr(q, q.correct_option),
                })

            # Save QuizResult
            QuizResult.objects.create(
                user=request.user,
                topic=topic,
                score=score,
                total_questions=len(questions)
            )

            return render(request, 'result.html', {
    'score': score,
    'total': len(questions),
    'half': len(questions) // 2,  # Add this line
    'topic': dict(Question.TOPIC_CHOICES).get(topic, topic),
    'results': results,
})

    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'form': form, 'topic': topic})


# General quiz view (all topics combined)
@login_required
def quiz_view(request):
    questions = Question.objects.all()
    if not questions.exists():
        return render(request, 'no_questions.html', {'topic': 'All Topics'})

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            for q in questions:
                selected = form.cleaned_data.get(f'question_{q.id}')
                if selected == q.correct_option:
                    score += 1

            # Save QuizResult
            QuizResult.objects.create(
                user=request.user,
                topic=questions.first().topic if questions.exists() else 'unknown',
                score=score,
                total_questions=len(questions)
            )

            return render(request, 'result.html', {
                'score': score,
                'total': len(questions),
                'topic': 'All Topics'
            })
    else:
        form = QuizForm(questions=questions)

    return render(request, 'quiz_detail.html', {'form': form, 'topic': 'All Topics'})

# Custom login view
class UserLoginView(LoginView):
    template_name = 'login.html'

# Custom logout view
class UserLogoutView(LogoutView):
    next_page = 'public_home'
