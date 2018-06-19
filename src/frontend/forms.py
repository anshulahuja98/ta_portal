from django import forms
from accounts.models import FeedbackTeachingAssistant


class ApprovalForm(forms.ModelForm):
    class Meta:
        model = FeedbackTeachingAssistant
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        kwargs.update(initial={
            'teaching_assistant': kwargs.pop('teaching_assistant', None),
            'course': kwargs.pop('course', None)
        })
        super().__init__(args, kwargs)
