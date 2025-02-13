from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.core.cache import cache
from django.shortcuts import redirect

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'proskmax@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)

def custom_logout(request):
    cache.delete('product_list')
    logout(request)
    return redirect('')



