from django.views.generic import ListView
from django.shortcuts import render
from .models import csgo, lol

from .tasks import stats_user_cs


class HomePageView(ListView):
    template_name = 'stats/statscsgo.html'
    context_object_name = 'stats'
    # assign "News" object list to the object "articles"
    # pass news objects as queryset for listview

    def get_queryset(self):
        return csgo.objects.all()


def stats_csgo(request):
    stats_cs = csgo.objects.all()
    return render(request, 'stats/stats_csgo.html', {'stats_cs': stats_cs})


def stats_lol(request):
    stats_lol = lol.objects.all()
    return render(request, 'stats/stats_lol.html', {'stats_lol': stats_lol})
