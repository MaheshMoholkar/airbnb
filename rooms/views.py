# from django.shortcuts import redirect
# from django.core.paginator import Paginator, EmptyPage

from pytz import timezone
from . import models
from django.views.generic import ListView
from django.shortcuts import render


class HomeView(ListView):

    """ HomeView Definition """
    
    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"
    context_object_name = "rooms"

    # def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
    #     context = super().get_context_data(**kwargs)
    #     now = timezone.now()
    #     context["now"] = now
    #     return context
    

def room_detail(request, pk):

    return render(request, "rooms/detail.html")


# Create your views here.
# def all_rooms(request):
#     page = request.GET.get("page", 1)
#     room_list = models.Room.objects.all()
#     paginator = Paginator(room_list, 10, orphans=5)
#     try:
#         rooms = paginator.page(int(page))
#         return render(request, "rooms/home.html",{"page":rooms})
#     except EmptyPage:
#         return redirect("/")
