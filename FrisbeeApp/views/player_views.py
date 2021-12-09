from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect, redirect, reverse)
from FrisbeeApp.models import Player
from FrisbeeApp.forms.player_form import PlayerForm

def create_view(request):
    context = {}
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "FrisbeeApp/PlayerTemplates/create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = Player.objects.all()
    return render(request, "FrisbeeApp/PlayerTemplates/list_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = Player.objects.get(id=id)
    return render(request, "FrisbeeApp/PlayerTemplates/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(League, id=id)
    form = PlayerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse(list_view), permanent=True)
    context["form"] = form
    return render(request, "FrisbeeApp/PlayerTemplates/update_view.html", context)
