from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User
class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs=
                                                      {"class": "input ",
                                                       "type": "text",
                                                       "placeholder": "Enter Username ",

                                                       }))
    email = forms.CharField(widget=forms.TextInput(attrs=
                                                   {"class": "input ",
                                                    "type": "email",
                                                    "placeholder": "Enter Email ",

                                                    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs=
                                                       {"class": "input ",
                                                        "type": "password",
                                                        "placeholder": "Entre Password ",

                                                        }))

    password2 = forms.CharField(widget=forms.TextInput(attrs=
                                                       {"class": "input ",
                                                        "type": "password",
                                                        "placeholder": "Confirm Password ",

                                                        }))
    name = forms.CharField(widget=forms.TextInput(attrs=
                                                  {"class": "input ",
                                                   "type": "text",
                                                   "placeholder": "Enter Name ",

                                                   }))
    city = forms.CharField(widget=forms.TextInput(attrs=
                                                  {"class": "input ",
                                                   "type": "text",
                                                   "placeholder": "Enter City ",

                                                   }), label="")
class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs=
                                                      {"class": "input ",
                                                       "type": "text",
                                                       "placeholder": "Enter username ",

                                                       }),)
    password1 = forms.CharField(widget=forms.TextInput(attrs=
                                                      {"class": "input ",
                                                       "type": "password",
                                                       "placeholder": "Enter Password ",

                                                       }))




    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(email)
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered. Please use a different email.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match. Please enter the same password in both fields.")

        return cleaned_data


    class Meta:
        model=User
        fields=['username','email','password1','password2','name','city']
