from django.shortcuts import render
from django.views import generic

from . import forms
from . import models

# Create your views here.


class AddPersonFormView(generic.FormView):
    template_name = "webApp/index.html"
    form_class = forms.AddPersonForm

    # Save the form
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IndexView(generic.ListView):
    model = models.Person
    template_name = 'webApp/list_view.html'
    context_object_name = 'all_persons'


def success(request):
    return render(request, "webApp/success.html", {})
