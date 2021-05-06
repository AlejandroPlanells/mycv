from django.shortcuts import render
from django.views.generic import TemplateView


class InicioPageView(TemplateView):
    template_name = 'paginas/inicio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inicio'] = "t"
        return context


class SobreMiPageView(TemplateView):
    template_name = 'paginas/sobremi.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sobremi'] = "t"
        return context


class ResumenPageView(TemplateView):
    template_name = 'paginas/resumen.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumen'] = "t"
        return context


class ContactarPageView(TemplateView):
    template_name = 'paginas/contacta.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contactar'] = "t"
        return context