from django.forms import ModelForm, Form, CharField, IntegerField
from .models import Livre


class LivreForm(ModelForm):
    class Meta:
        model = Livre
        fields = '__all__'


class RawLivreForm(Form):
    titre = CharField(max_length=255)
    tome = IntegerField()
    auteur = CharField(max_length=255)
    serie = CharField(max_length=255)
    genre = CharField(max_length=55)
    image_url = CharField(max_length=2085)
