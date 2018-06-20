from django import forms
from accounts.models import FeedbackTeachingAssistant


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = FeedbackTeachingAssistant
        fields = '__all__'
