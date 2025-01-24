from django.shortcuts import render, redirect, get_object_or_404
from .models import Marker
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Marker
from .serializers import MarkerSerializer
from django.http import JsonResponse
from django.core.serializers import serialize
from .forms import AddMarker
from . import forms


def map_view(request):
    markers = Marker.objects.all()

    # Serialize data for safe usage in JS.
    serialized_markers = serialize('json', markers)

    # Debugging: Print serialized data in the console
    print(serialized_markers)

    return render(request, 'mapapp/map.html', {'markers': serialized_markers})


class MarkerListView(APIView):
    def get(self, request):
        markers = Marker.objects.all()
        serializer = MarkerSerializer(markers, many=True)
        return Response(serializer.data)


# def marker_info(request, pk):
#     marker = get_object_or_404(Marker, pk=pk)

#     return render(request, 'mapapp/info.html', {'marker': marker})

def marker_info(request, pk):
    # Get marker object by primary key
    marker = get_object_or_404(Marker, pk=pk)

    # Render the info page template with marker details
    return render(request, 'mapapp/info.html', {'marker': marker})


def map_view(request):
    # Serialize marker data to JSON
    markers = Marker.objects.all()
    serialized_markers = serialize('json', markers)

    # Pass the serialized data to the template
    return render(request, 'mapapp/map.html', {'markers': serialized_markers})


# @login_required(login_url="/users/login/")
# def marker(request):
#     if request.method == 'POST':
#         form = AddMarker(request.POST, request.FILES)
#         if form.is_valid():
#             newpost = form.save(commit=False)
#             newpost.author = request.user
#             newpost.save()
#             return redirect('historic:map')
#         else:
#             print(form.errors)  # Debugging: Print form validation errors
#     else:
#         form = AddMarker()
#     return render(request, 'mapapp/new-marker.html', {'form': form})


@login_required(login_url="/users/login/")
def marker(request):
    if request.method == 'POST':
        print("POST data:", request.POST)  # Debug form data
        print("FILES data:", request.FILES)  # Debug uploaded files
        form = AddMarker(request.POST, request.FILES)
        if form.is_valid():
            print("Form is valid")  # Debug
            newpost = form.save(commit=False)
            newpost.author = request.user  # Automatically set the author
            newpost.save()
            return redirect('historic:map')
        else:
            print("Form errors:", form.errors)  # Debug
            # Return errors for easier debugging
            return JsonResponse({"errors": form.errors}, status=400)
    else:
        print("GET request received")  # Debug
        form = AddMarker()
    return render(request, 'mapapp/new_marker.html', {'form': form})
