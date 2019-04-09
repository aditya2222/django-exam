from django.shortcuts import render
from django.views import generic
from . import models
from django.template import RequestContext
from . import serializers
from rest_framework import generics

# Create your views here.

# list view for categories


class HomePageView(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategoriesSerializer

# list view for question papers


class QuestionPaperView(generics.ListAPIView):
    model = models.QuestionPaper
    template_name = 'questionpaper_list.html'
    serializer_class = serializers.QuestionPapersSerialzer

    def get_queryset(self, *args, **kwargs):
        queryset = models.QuestionPaper.objects.filter(
            category__name__contains=self.kwargs['name'])
        return queryset

# list view for questions


class QuestionsUpdateView(generics.ListAPIView):
    model = models.Questions
    serializer_class = serializers.QuestionsSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = models.Questions.objects.filter(
            questionPaper__name__contains=self.kwargs['name'])
        return queryset

# updating api view for posting answers


class QuestionsModifyView(generics.UpdateAPIView):
    model = models.Questions
    serializer_class = serializers.QuestionsSerializer
    queryset = models.Questions.objects.all()

# list view for getting questions with a subejct


class SubjectsList(generics.ListAPIView):
    model = models.Questions
    serializer_class = serializers.QuestionsSerializer

    def get_queryset(self, *args, **kwargs):
        print(self.kwargs)
        queryset = models.Questions.objects.filter(
            subjects__name__contains=self.kwargs['subjects'], questionPaper__name__contains=self.kwargs['questionpaper'])
        return queryset

# List view for all subjects


class SubjectsListView(generics.ListAPIView):
    serializer_class = serializers.SubjectsSerailzer
    queryset = models.Subjects.objects.all()
