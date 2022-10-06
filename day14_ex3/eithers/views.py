from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse, HttpResponseForbidden
from .models import Question, Comment
from .forms import QuestionForm, CommentForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    context = {
        'questions': questions,
    }

    return render(request, 'eithers/index.html', context)



@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save()
            return redirect('eithers:detail', question.pk)
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


def random(request):
    pass

def detail(request, question_pk):
    question = Question.objects.get(pk=question_pk)
    comment_form = CommentForm()
    comments = question.comment_set.all()
    context = {
        'question' : question,
        'comment_form':comment_form,
        'comments' : comments,
    }
    return render(request, 'eithers/detail.html', context)
    

def create_comment(request, pk):
    pass



