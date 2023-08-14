from django.forms import ModelForm
from home.models import Contact


class UpdateForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
