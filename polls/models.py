import datetime

from django.db import models
from django.utils import timezone

# Each Model is represented by a class that subclasses django.db.models.Model
class Question(models.Model):
    # Class variables reprent a database field in the model
    # question_text is the name of the Field instance
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # This allows returns the actual question, instead of just "Question object"
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # Choice.question is a relationship because of .ForeignKey and tells django
    # that each Choice is related to a single Question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote_tally = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text