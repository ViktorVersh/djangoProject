from django.shortcuts import render
from django.http import HttpResponse
# from .forms import ContactForm


# Create your views here.
def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subscribe = request.POST.get('subscribe') == 'on'

        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")
        print(f"Subscribe: {subscribe}")

        return HttpResponse("Форма успешно отправлена!")

    return render(request, 'index.html')

# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             message = form.cleaned_data['message']
#             subscribe = form.cleaned_data['subscribe']
#     else:
#         form = ContactForm()
#     return render(request, 'index.html', {'form': form})
