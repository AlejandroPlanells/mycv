from django.views.generic import ListView
from django.shortcuts import render
from .models import Stats

from .tasks import stats_user

class HomePageView(ListView):
    template_name = 'test.html'
    context_object_name = 'stats'
    # assign "News" object list to the object "articles"
    # pass news objects as queryset for listview

    def get_queryset(self):
        return Stats.objects.all()


def test(request):
    print("iniciado")
    stats = Stats.objects.all()
    return render(request,
                  'test.html',
                  {'stats': stats})
