from django import forms
from . import models


class KeepFrameForm(forms.Form):
    height = forms.IntegerField(label='Height (cm)', min_value=1)
    width = forms.IntegerField(label='Width (cm)', min_value=1)
    mechanism = forms.ChoiceField(
        label='Opening Mechanism',
        choices=[
            ('hinged', 'Hinged'),
            ('sliding', 'Sliding'),
            ('other', 'Other')
        ]
    )
    wings = forms.IntegerField(label='Number of Wings', min_value=1)
    pos_hinge_top = forms.IntegerField(
        label='Position of top hinge (cm)', min_value=0)
    pos_hinge_middle = forms.IntegerField(
        label='Position of middle hinge (cm)')
    pos_hinge_bottom = forms.IntegerField(
        label='Position of bottom hinge (cm)', min_value=0)
    pos_lock = forms.IntegerField(
        label='Position of Lock (cm)', min_value=0)


class NewFrameForm(forms.Form):
    height = forms.IntegerField(label='Height (cm)', min_value=1)
    width = forms.IntegerField(label='Width (cm)', min_value=1)
    opening_mechanism = forms.ChoiceField(
        label='Opening Mechanism',
        choices=[
            ('sliding', 'Sliding'),
            ('hinged', 'Hinged'),
            ('other', 'Other')
        ]
    )
    wings = forms.IntegerField(label='Number of Wings', min_value=1)


class AddNewDoor(forms.ModelForm):
    class Meta:
        model = models.Door
        fields = ['image', 'title', 'height', 'width', 'pos_hinge_top', 'pos_hinge_middle',
                  'pos_hinge_bottom', 'pos_lock', 'material', 'wings', 'mechanism', 'frame', 'opening_height', 'opening_width', 'details', 'contact']
        labels = {
            "height": ("Height (cm)"),
            "width": ("Width (cm)"),
            "pos_hinge_top": ("Position of top hinge (cm)"),
            "pos_hinge_middle": ("Position of middle hinge (cm)"),
            "pos_hinge_bottom": ("Position of bottom hinge (cm)"),
            "pos_lock": ("Position of lock (cm)"),
            "mechanism": ("Opening mechanism"),
            "frame": ("Does the door come with a useable frame?"),
            "opening_height": ("Opening height"),
            "opening_width": ("Opening width"),
            "details": ("Details"),
            "contact": ("Contact information"),
        }
