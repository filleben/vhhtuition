from django import forms
from .models import Assessment, Question


class AssessmentForm(forms.ModelForm):
    """
    Assessment Form
    """
    class Meta:
        model = Assessment
        fields = '__all__'


class QuestionForm(forms.ModelForm):
    """
    Question Form
    Uses the name field from assessment model as a drop down menu
    """
    class Meta:
        model = Question
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        assessment = Assessment.objects.all()
        name = [(a.id, a.get_name()) for a in assessment]

        self.fields['assessment'].choices = name
