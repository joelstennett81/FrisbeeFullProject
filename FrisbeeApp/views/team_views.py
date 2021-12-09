from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect, redirect, reverse)
from FrisbeeApp.models import Team
from FrisbeeApp.forms.team_form import TeamForm

def create_view(request):
    context = {}
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    return render(request, "FrisbeeApp/TeamTemplates/create_view.html", context)

def list_view(request):
    context = {}
    context["dataset"] = Team.objects.all()
    return render(request, "FrisbeeApp/TeamTemplates/list_view.html", context)

def detail_view(request, id):
    context = {}
    context["data"] = Team.objects.get(id=id)
    return render(request, "FrisbeeApp/TeamTemplates/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(League, id=id)
    form = TeamForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse(list_view), permanent=True)
    context["form"] = form
    return render(request, "FrisbeeApp/TeamTemplates/update_view.html", context)
