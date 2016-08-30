from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.utils import timezone


# Database model for Questions
@python_2_unicode_compatible
class Question(models.Model):
    def __str__(self):
        return self.question_text

    # Demo function to return datetime
    def was_published_recently(self):
        return self.pub_Date >= timezone.now() - datetime.timedelta(days=1)
    question_text = models.CharField(max_length=200)
    pub_Date = models.DateTimeField('date published')


# Database model for choice
@python_2_unicode_compatible
class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
