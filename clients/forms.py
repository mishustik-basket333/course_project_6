from clients.models import Client, Mail, Mailings, Log
from django import forms


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = '__all__'


class MailingsForm(forms.ModelForm):
    class Meta:
        model = Mailings
        fields = '__all__'


class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = '__all__'

