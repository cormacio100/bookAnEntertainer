from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User
from django.core.exceptions import ValidationError


#   CUSTOM REGISTRATION FORM
class UserRegistrationForm(UserCreationForm):
    YES_NO = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    USER_TYPE = (
        'Entertainer', 'Entertainer',
        'Event_Organiser', 'Event_Organiser',
    )
    COUNTIES = (
        ('Antrim', 'Antrim'),
        ('Armagh', 'Armagh'),
        ('Carlow', 'Carlow'),
        ('Cavan', 'Cavan'),
        ('Clare', 'Clare'),
        ('Cork', 'Cork'),
        ('Derry', 'Derry'),
        ('Donegal', 'Donegal'),
        ('Down', 'Down'),
        ('Dublin', 'Dublin'),
        ('Fermanagh', 'Fermanagh'),
        ('Galway', 'Galway'),
        ('Kerry', 'Kerry'),
        ('Kildare', 'Kildare'),
        ('Kilkenny', 'Kilkenny'),
        ('Laois', 'Laois'),
        ('Leitrim', 'Leitrim'),
        ('Limerick', 'Limerick'),
        ('Longford', 'Longford'),
        ('Louth', 'Louth'),
        ('Mayo', 'Mayo'),
        ('Meath', 'Meath'),
        ('Monaghan', 'Monaghan'),
        ('Offaly', 'Offaly'),
        ('Roscommon', 'Roscommon'),
        ('Sligo', 'Sligo'),
        ('Tipperary', 'Tipperary'),
        ('Tyrone', 'Tyrone'),
        ('Waterford', 'Waterford'),
        ('Westmeath', 'Westmeath'),
        ('Wexford', 'Wexford'),
        ('Wicklow', 'Wicklow'),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    '''
    location = forms.CharField(
        label='location',
        widget=forms.Select(choices=COUNTIES)
    )
    

    user_type = forms.CharField(
        label='User Type',
        widget=forms.Select(choices=USER_TYPE)
    )
    '''
    is_entertainer = forms.CharField(
        label='Is an Entertainer?',
        widget=forms.Select(choices=YES_NO)
    )


    #   THE FIELDS WE WANT TO DISPLAY
    #   EMAIL and USERNAME are default USER attributes - also first_name and last_name
    #   In this case PASSWORD1 and PASSWORD2 have been customised
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        exclude = ['username']

    #   clean the passwords and ensure they are valid
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        #   to be valid the passwords must match
        if password1 and password2 and password1 != password2:
            message = "Passwords do not match"
            raise ValidationError(message)

        return password2

    #   For custom User Authorisation that looks for email instead of username, we will need to override the default
    #   save method as the username attrib cannot be left empty. Set it equal to the email
    def save(self, commit=True):
        #   .save(commit=False) prevents teh form from auto saving
        instance = super(UserRegistrationForm, self).save(commit=False)

        #   automatically set USERNAME to email address to create a unique identifier
        instance.username = instance.email

        if commit:
            instance.save()

        return instance


#   SIMPLE LOG IN FORM
class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)