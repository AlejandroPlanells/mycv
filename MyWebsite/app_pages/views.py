from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.contrib.auth.models import User

import json

# Contacto
from django.template.loader import render_to_string
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm
# ----------------------

from .serializers import UserSerailizer


class InicioPageView(TemplateView):
    template_name = 'paginas/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inicio'] = "inicio"
        return context


class SobreMiPageView(TemplateView):
    template_name = 'paginas/sobremi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sobremi'] = "sobremi"
        return context


class ResumenPageView(TemplateView):
    template_name = 'paginas/resumen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumen'] = "resumen"
        return context


class ContactarPageView(TemplateView):
    template_name = 'paginas/contacta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_form'] = ContactForm
        context['contactar'] = "contactar"
        return context

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto')
        mensaje = request.POST.get('mensaje')

        body = render_to_string(
            'paginas/contenido_email.html', {
                'nombre': nombre,
                'email': email,
                'asunto': asunto,
                'mensaje': mensaje,
            },
        )

        email_message = EmailMessage(
            subject=asunto,
            body=body,
            from_email=email,
            to=['alex10planells@gmail.com']
        )
        email_message.content_subtype = 'html'
        email_message.send()
        messages.info(request, 'Tu email se ha enviado correctamente, sera revisado lo antes posible, gracias!')

        return redirect('app_pages:inicio')


def userSettings(request):
    user, created = User.objects.get_or_create(id=1)
    setting = user.setting

    seralizer = UserSerailizer(setting, many=False)

    return JsonResponse(seralizer.data, safe=False)


def updateTheme(request):
    data = json.loads(request.body)
    theme = data['theme']

    user, created = User.objects.get_or_create(id=1)
    user.setting.value = theme
    user.setting.save()
    print('Request:', theme)
    return JsonResponse('Updated..', safe=False)