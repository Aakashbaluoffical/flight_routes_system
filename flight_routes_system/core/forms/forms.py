from django import forms
from core.models.airport_models import Airports



# class SearchForm(forms.Form):

#     class Meta:
#         model = Airports
#         fields = "__all__"


class AirportForm(forms.Form):
    class Meta:
        model = Airports
        fields = "__all__"
