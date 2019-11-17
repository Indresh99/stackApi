import requests
from bs4 import BeautifulSoup
import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Question
from .serializer import QuestionSerializer


# Create your views here.

def index(request):
    return HttpResponse("<h1>Success</h1>")


class QuestionAPI(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


def latest(request):
    try:
        res = requests.get("https://stackoverflow.com/questions")
        soup = BeautifulSoup(res.text, "html.parser")

        questions = soup.select(".question-summary")
        for e in questions:
            questionsq = e.select_one('.question-hyperlink').getText()
            vote_count = e.select_one('.vote-count-post').getText()
            views = e.select_one('.views').attrs['title']
            tags = [i.getText() for i in (e.select('.post-tag'))]

            question = Question()
            question.question = questionsq
            question.view_count = vote_count
            question.views = views
            question.tags = tags

            question.save()

        return HttpResponse("Data Fetched")
    except e as Exception:
        return HttpResponse(f'Failed {e}')
