from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect, redirect, reverse)
from FrisbeeApp.models import Game
from FrisbeeApp.forms.game_form import GameForm

def create_view(request):
    context = {}
    form = GameForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "FrisbeeApp/GameTemplates/create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = Game.objects.all()
    return render(request, "FrisbeeApp/GameTemplates/list_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = Game.objects.get(id=id)
    return render(request, "FrisbeeApp/GameTemplates/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(Game, id=id)
    form = GameForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse(list_view), permanent=True)
    context["form"] = form
    return render(request, "FrisbeeApp/GameTemplates/update_view.html", context)

