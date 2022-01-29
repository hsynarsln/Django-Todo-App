from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        # fields = ["first_name", "last_name", "number"]
        # ! yukarıdaki gib yazmak yerine tüm fieldları kullanmak için bu şekilde yazabiliriz.
        fields = "__all__"
        # labels = {"first_name": "Adınız",
        #           "last_name": "Soyadınız", "number": "Numaranız"}
