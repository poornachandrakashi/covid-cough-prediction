from django.forms import ModelForm
from app.models import Response


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        exclude = []
