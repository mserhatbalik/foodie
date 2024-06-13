"""
This module defines the UserForm class, a subclass of Django's forms.ModelForm.

The UserForm class is used to create and update instances of the User model. It includes fields for the user's first name, last name, username, email, and password.

The password and confirm_password fields use Django's PasswordInput widget. This widget renders an HTML input element with type="password", which means the input will be masked for privacy.

The Meta class inside UserForm provides options for the ModelForm. It specifies that this form is for the User model and lists the fields that should be included in the form.

Imported Modules:
    - django.forms: Used to create form classes and fields.
    - accounts.models: Used to import the User model.

Classes:
    - UserForm: A form for creating and updating User instances.
"""
# Import the necessary modules
from django import forms
from accounts.models import User

# Define the UserForm class, which is a subclass of forms.ModelForm
class UserForm(forms.ModelForm):
    # Define a password field. The widget=forms.PasswordInput() argument specifies that this field should use the PasswordInput widget.
    # This widget renders an HTML input element with type="password", which means the input will be masked.
    password = forms.CharField(widget=forms.PasswordInput())

    # Define a confirm_password field, similar to the password field.
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    # The Meta class is used to provide options for the ModelForm.
    class Meta:
        # Specify that this form is for the User model.
        model = User

        # Specify the fields that should be included in the form. These fields correspond to the fields defined in the User model.
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def clean(self):
        # Retrieve the cleaned data from the form
        cleaned_data = super(UserForm, self).clean()

        # Retrieve the password and confirm_password fields from the cleaned data
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        # Check if the password and confirm_password fields match
        if password != confirm_password:
            # If they don't match, raise a validation error
            raise forms.ValidationError("Passwords do not match")