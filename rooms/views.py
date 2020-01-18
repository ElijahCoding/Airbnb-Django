from django.views.generic import ListView
from . import models
from django.shortcuts import render


class HomeView(ListView):
    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/detail.html")