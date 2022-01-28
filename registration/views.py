from django.shortcuts import render, HttpResponse
from .forms import MemberForm


def home_view(request):
    context = {}

    # create object of form
    form = MemberForm(request.POST or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        program = form.cleaned_data["program"]
        context['program'] = program
        return render(request, "success.html", context)

    context['form'] = form
    return render(request, "form.html", context)