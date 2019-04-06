from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class QuestionPaper(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name


class Questions(models.Model):
    questionPaper = models.ForeignKey(QuestionPaper, on_delete=models.CASCADE)
    questionText = models.CharField(max_length=120, blank=True, null=True)
    questionImage = models.ImageField(blank=True, null=True)
    option1text = models.CharField(max_length=120,
                                   blank=True, null=True)
    option1image = models.ImageField(blank=True, null=True)
    option2text = models.CharField(max_length=120, blank=True, null=True)
    option2image = models.ImageField(blank=True, null=True)
    option3text = models.CharField(max_length=120, blank=True, null=True)
    option3image = models.ImageField(blank=True, null=True)
    option4text = models.CharField(max_length=120, blank=True, null=True)
    option4image = models.ImageField(blank=True, null=True)
    correctAnswer = models.CharField(max_length=120, blank=True, null=True)
    explanation = models.TextField(blank=True, null=True)
    answer = models.CharField(
        max_length=120, blank=True, null=True)
