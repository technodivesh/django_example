from django.contrib import admin

# Register your models here.
from . models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

	# Describing Fieldset for Add-Question page, else default page will come 
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    # Add Choice option itself in Add-Question page, No need to go on Add-Choice page
    inlines = [ChoiceInline] 

    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']  # Add Filter column on Admin Question page

    # It adds search box on Admin Question page
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

