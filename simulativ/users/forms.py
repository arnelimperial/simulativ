from django.forms import CharField, EmailField, TextInput, Form, EmailInput, PasswordInput
from django.contrib.auth import forms, get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from allauth.account.forms import SignupForm
from django.utils.safestring import mark_safe
# from django import forms
User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name")


class UserCreationForm(forms.UserCreationForm):
    first_name = CharField(required=True, widget=TextInput)
    last_name = CharField(required=True, widget=TextInput)

    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class CustomSignupForm(SignupForm):
    first_name = CharField(max_length=100, required=True, widget=TextInput)
    last_name = CharField(max_length=100, required=True, widget=TextInput)
    username = CharField(max_length=50, widget=TextInput)
    email = EmailField(required=True, widget=EmailInput)
    password1 = CharField(widget=PasswordInput)
    password2 = CharField(widget=PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = CharField(required=True)
        self.fields['last_name'] = CharField(required=True)
        #self.fields['tos'] = BooleanField(required=True)
        #self.fields['tos'].label = mark_safe(_('I have read and agreed with the <a href="{0}" class="text-primary">Terms and Conditions</a> and <a href={1} class="text-primary">Privacy Policy</a>.'))

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.save()

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        return user

# class CustomSignupForm(Form):
#     first_name = CharField(max_length=100, required=True, widget=TextInput)
#     last_name = CharField(max_length=100, required=True, widget=TextInput)
#     username = CharField(max_length=50, widget=TextInput)
#     email = EmailField(required=True, widget=EmailInput)
#     password1 = CharField(widget=PasswordInput)
#     password2 = CharField(widget=PasswordInput)
#
#     def signup(self, request, user):
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.username = self.cleaned_data['username']
#         user.email = self.cleaned_data['email']
#         user.save()
#         return user






