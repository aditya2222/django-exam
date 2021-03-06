from rest_framework import serializers
from . import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class QuestionPapersSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.QuestionPaper
        fields = '__all__'


class QuestionsSerializer(serializers.ModelSerializer):
    subject_name = serializers.ReadOnlyField(source='subjects.name')

    class Meta:
        model = models.Questions
        fields = '__all__'


class SubjectsSerailzer(serializers.ModelSerializer):
    class Meta:
        model = models.Subjects
        fields = '__all__'
