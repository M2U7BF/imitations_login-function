from django.contrib.auth import forms as auth_forms

class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self,*args, **kw):
        super().__init__(*args,**kw)
        for field in self.fields.values():
            field.widget.attrs['placeolder'] = field.label