"""
This module defines the registerUser view function.

The registerUser function is responsible for handling the registration process for a new user. It checks if the request method is POST, and if so, creates a UserForm instance with the data from the request, validates the form data, sets the user's role to CUSTOMER, saves the form data to the database, and then redirects the user to the registerUser page. If the request method is not POST, it creates an empty UserForm instance and renders the registerUser.html template with the form data.

Imported Modules:
    - django.http: Used to import the HttpResponse class.
    - django.shortcuts: Used to import the render and redirect functions.
    - accounts.forms: Used to import the UserForm class.
    - accounts.models: Used to import the User model.

Functions:
    - registerUser: A view function for handling the registration process for a new user.
"""
# Import necessary modules and classes
from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.forms import UserForm
from accounts.models import User

# registerUser function will be called when /accounts/registerUser/ path is accessed, which is defined in accounts/urls.py
def registerUser(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # If it is POST, create a UserForm instance with the data from the request
        form = UserForm(request.POST)
        # Check if the form data is valid
        if form.is_valid():
            # If it is valid, save the form data but don't commit to the database yet
            user = form.save(commit=False)
            # Set the user's role to CUSTOMER
            user.role = User.CUSTOMER
            # Now commit the data to the database
            form.save()
            # Redirect the user to the registerUser page
            return redirect('registerUser')
    else:
        # If the request method is not POST, create an empty UserForm instance
        form = UserForm()
    # Create a context dictionary to pass data to the template
    context = {'form': form}
    # Render the registerUser.html template with the context data
    return render(request, 'accounts/registerUser.html', context)