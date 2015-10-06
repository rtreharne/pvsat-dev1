from django import forms
from time import time
from message.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ('email', 'subject', 'first_name', 'last_name', 'message')
