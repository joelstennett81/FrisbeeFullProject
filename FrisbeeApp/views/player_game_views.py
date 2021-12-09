from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect, redirect, reverse)
from FrisbeeApp.models import PlayerGame
from FrisbeeApp.forms.player_game_form import PlayerGameForm

def create_view(request):
    context = {}
    form = PlayerGameForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "FrisbeeApp/PlayerGameTemplates/create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = PlayerGame.objects.all()
    return render(request, "FrisbeeApp/PlayerGameTemplates/list_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = PlayerGame.objects.get(id=id)
    return render(request, "FrisbeeApp/PlayerGameTemplates/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(League, id=id)
    form = PlayerGameForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse(list_view), permanent=True)
    context["form"] = form
    return render(request, "FrisbeeApp/PlayerGameTemplates/update_view.html", context)
