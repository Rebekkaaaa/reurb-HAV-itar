# from .forms import SizeSearchForm
from django.shortcuts import render, redirect, get_object_or_404

from .models import Door
from . import forms
from .forms import KeepFrameForm, NewFrameForm, AddNewDoor
# from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.


def current(request):
    return render(request, 'current.html')


def keep_frame(request):
    if request.method == 'POST':
        form = forms.KeepFrameForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # For example, save it to the database or perform calculations
            pass
    else:
        form = forms.KeepFrameForm()

    return render(request, 'keep_frame.html', {'form': form})


def new_frame(request):
    if request.method == 'POST':
        form = forms.NewFrameForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data as required
            # For example, save it to the database or perform calculations
            pass
    else:
        form = forms.NewFrameForm()

    return render(request, 'new_frame.html', {'form': form})


def search_view(request):
    if request.method == 'POST':
        form = KeepFrameForm(request.POST)
        if form.is_valid():

            # Extract cleaned data from the form
            height = form.cleaned_data['height']
            width = form.cleaned_data['width']
            pos_hinge_top = form.cleaned_data['pos_hinge_top']
            pos_hinge_middle = form.cleaned_data['pos_hinge_middle']
            pos_hinge_bottom = form.cleaned_data['pos_hinge_bottom']
            pos_lock = form.cleaned_data['pos_lock']
            wings = form.cleaned_data['wings']
            # mechanism = form.cleaned_data['mechanism']

            # Check if a door with similar data already exists
            results = Door.objects.filter(
                Q(height__gte=height, height__lte=height + 5) &
                Q(width__gte=width, width__lte=width + 5) &
                Q(pos_hinge_top__gte=pos_hinge_top, pos_hinge_top__lte=pos_hinge_top + 5) &
                Q(pos_hinge_middle__gte=pos_hinge_middle, pos_hinge_middle__lte=pos_hinge_middle + 5) &
                Q(pos_hinge_bottom__gte=pos_hinge_bottom, pos_hinge_bottom__lte=pos_hinge_bottom + 5) &
                Q(pos_lock__gte=pos_lock, pos_lock__lte=pos_lock + 5) &
                Q(wings=wings)
                # Q(mechanism=mechanism)
            )

            if results:
                # Door already exists
                return render(request, 'door_matches.html', {'results': results})

            # Redirect to a list of doors or another relevant page
            return render(request, 'door_matches.html', {'results': results})
    else:
        form = KeepFrameForm()

    return render(request, 'keep_frame.html', {'form': form, 'results': results})


def new_frame_view(request):
    results = None  # Default value for results
    if request.method == 'POST':
        form = NewFrameForm(request.POST)
        if form.is_valid():

            # Extract cleaned data from the form
            opening_height = form.cleaned_data['height']
            opening_width = form.cleaned_data['width']
            wings = form.cleaned_data['wings']
            # mechanism = form.cleaned_data['mechanism']

            # Check if a door with similar data already exists
            results = Door.objects.filter(
                Q(height__gte=opening_height, height__lte=opening_height + 5) &
                Q(width__gte=opening_width, width__lte=opening_width) &
                Q(wings=wings)
                # Q(mechanism=mechanism)
            )

            if results:
                # Door already exists
                return render(request, 'door_matches.html', {'results': results})

            # Redirect to a list of doors or another relevant page
            return render(request, 'door_matches.html', {'results': results})
    else:
        form = NewFrameForm()

    return render(request, 'new_frame.html', {'form': form, 'results': results})


def doors_list(request):
    door = Door.objects.all().order_by('-date')
    return render(request, 'doors/doors_list.html', {'doors': door})


# def doors_page(request):
#     door = Door.objects.get()
#     return render(request, 'doors/doors_page.html', {'doors': door})

def doors_page(request, pk):
    # Get door object by primary key
    door = get_object_or_404(Door, pk=pk)

    # Render the info page template with door details
    return render(request, 'doors/doors_page.html', {'doors': door})


@login_required(login_url="/users/login/")
def door_new(request):
    if request.method == 'POST':
        form = AddNewDoor(request.POST, request.FILES)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.author = request.user
            newpost.save()
            return redirect('current:list')
    else:
        form = forms.AddNewDoor()
    return render(request, 'doors/add_door.html', {'form': form})


@login_required(login_url="/users/login/")
def my_doors(request):
    # Filter doors by the logged-in user
    door = Door.objects.filter(user=request.user)
    return render(request, 'doors/my_doors.html', {'doors': door})


@login_required(login_url="/users/login/")
def edit_door(request, pk):
    # Ensure door belongs to the user
    door = get_object_or_404(Door, pk=pk, user=request.user)
    if request.method == 'POST':
        form = AddNewDoor(request.POST, request.FILES, instance=door)
        if form.is_valid():
            form.save()
            # Redirect to the user's doors list
            return redirect('current:my_doors')
    else:
        form = AddNewDoor(instance=door)
    return render(request, 'doors/edit_door.html', {'form': form})


@login_required(login_url="/users/login/")
def delete_door(request, pk):
    # Ensure door belongs to the user
    door = get_object_or_404(Door, pk=pk, user=request.user)
    if request.method == 'POST':
        door.delete()
        # Redirect to the user's doors list
        return redirect('current:my_doors')
    return render(request, 'doors/delete_door.html', {'door': door})
