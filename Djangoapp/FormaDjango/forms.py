from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Введите Ваше имя')
    email = forms.EmailField(label='email')
    message = forms.CharField(widget=forms.Textarea, label='Ваше сообщение')
    subscribe = forms.BooleanField(required=False, label='Подписаться на рассылку')
