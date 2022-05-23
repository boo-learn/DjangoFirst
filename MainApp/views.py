from django.shortcuts import render, HttpResponse, Http404
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    return render(request, "index.html")


def item_page(request, id):
    try:
        item = Item.objects.get(pk=id)
        context = {"item": item}
        return render(request, "item_page.html", context)
    except ObjectDoesNotExist:
        raise Http404(f"Товар c id={id} не найден")


def items_list(request):
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)