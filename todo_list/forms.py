from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from todo_list.models import Tag, Task


class BaseTaskDeadlineValidationForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["deadline"]

    def clean_deadline(self) -> str:
        deadline = self.cleaned_data["deadline"]
        if datetime.now() > deadline:
            raise ValidationError("Deadline is already expired! "
                                  f"You cannot set date earlier than {datetime.now()}")
        return deadline


class TaskCreateOrUpdateForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Task
        fields = "__all__"
        widgets = {
            "deadline": forms.DateTimeInput(
                format="%Y-%m-%dT%H:%M",
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "datetime-local"
                }
            ),

        }
