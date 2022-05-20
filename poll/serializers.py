from rest_framework import serializers
from poll.models import Question
from .models import Choice
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question 
        fields = ['id','question_text','pub_date']
        
class ChoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id','question','choice_text','votes']