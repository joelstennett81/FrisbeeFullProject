from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect, redirect, reverse)
from FrisbeeApp.models import League
from FrisbeeApp.forms.league_form import LeagueForm

def create_view(request):
    context = {}
    form = LeagueForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "FrisbeeApp/LeagueTemplates/create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = League.objects.all()
    return render(request, "FrisbeeApp/LeagueTemplates/list_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = League.objects.get(id=id)
    return render(request, "FrisbeeApp/LeagueTemplates/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(League, id=id)
    form = LeagueForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse(list_view), permanent=True)
    context["form"] = form
    return render(request, "FrisbeeApp/LeagueTemplates/update_view.html", context)