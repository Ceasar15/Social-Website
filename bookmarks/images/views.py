from django.http import request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm

@login_required
def image_create(request):
    if request.method == 'POST':
        # form is posted
        form = ImageCreateForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            messages.success(request, "Image is Uploaded")

            return redirect(new_item.get_absolute_url())
        
    else:
        form = ImageCreateForm(data=request.GET)

    template = 'images/image/create.html'
    context = {
        'section': 'images',
        'form': form,
    }
    return render(request, template, context)

