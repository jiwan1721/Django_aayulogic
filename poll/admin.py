from django.contrib import admin

# Register your models here.
from .models import Question, Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    
class questionAdmin(admin.ModelAdmin):
    #fields = ['pub_date','question_text']
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display= (
        'question_text',
        'pub_date'
     
    )
    
    
    
    
admin.site.register(Question,questionAdmin)
admin.site.register(Choice)
# polls laii admin panel ma add gareko

