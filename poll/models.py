from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_publisher_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    

class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    


# after this you have to type cmd " python manage.py makemigration poll"
# yo cmd hanyo vaney migration vittra 0001.py file banxa with code


#and then type "python manage,py migrate poll 0001"
# yo code ley model laii database ma migrate gardinxa