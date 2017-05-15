from django.shortcuts import render
from .forms import UserLeadForm
# Create your views here.
def landing_home(request):
    form = UserLeadForm(request.POST or None)
    post_request = False
    if form.is_valid:
        instance = form.save(commit=False)
        instance.save()

    if request.method == 'POST':
        post_request = True


    context = {
        "form": form,
        "submitted": post_request
    }

    return render(request, 'index.html', context)