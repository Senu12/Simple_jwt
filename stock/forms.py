from django.forms import ModelForm
from Table.models import Stocktick

class BookForm(ModelForm):
    class Meta:
        model = Stocktick
        fields = '__all__'