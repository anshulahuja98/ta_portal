from django import forms
from courses.models import Feedback


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
