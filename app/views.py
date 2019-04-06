from django.shortcuts import render
from django.views import generic
from . import models
from django.template import RequestContext

# Create your views here.


class HomePageView(generic.ListView):
    model = models.Category
    fields = '__all__'
    template_name = 'categories_list.html'
    success_url = '/'


class QuestionPaperView(generic.ListView):
    model = models.QuestionPaper
    template_name = 'questionpaper_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionPaperView, self).get_context_data(
            *args, **kwargs)
        question_papers_inside_category = models.QuestionPaper.objects.filter(
            category__name__contains=self.kwargs['name']).values()
        print(question_papers_inside_category)
        context['questionPapers'] = question_papers_inside_category
        return context


class QuestionsUpdateView(generic.ListView):
    model = models.Questions
    template_name = 'questionpaper_details.html'
    fields = ("answer",)
    success_url = '/'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):
        queryset = models.Questions.objects.filter(
            questionPaper__name__contains=self.kwargs['name'])
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionsUpdateView,
                        self).get_context_data(*args, **kwargs)
        context['context_instance'] = RequestContext(self.request)
        return context


class QuestionsModifyView(generic.UpdateView):
    model = models.Questions
    fields = ('answer',)
    template_name = 'update.html'
    success_url = '/'
