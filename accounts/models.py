# Importing necessary modules from Django
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# UserManager is a class that extends BaseUserManager. It is used to manage database queries for the User model.
class UserManager(BaseUserManager):
    # create_user is a method that takes in first name, last name, username, email, and password as parameters.
    # It creates and saves a User with the given parameters.
    def create_user(self, first_name, last_name, username, email, password=None):
        # If email is not provided, raise a ValueError
        if not email:
            raise ValueError('User must have an email address')
        # If username is not provided, raise a ValueError
        if not username:
            raise ValueError('User must have a username')

        # Create a User object with the given parameters
        user = self.model(
            email = self.normalize_email(email),  # Normalize the email by lowercasing the domain part of it
            username = username,
            first_name = first_name,
            last_name = last_name
        )

        # Set user's password
        user.set_password(password)
        # Save the user object into the database
        user.save(using=self._db)
        return user

    # create_superuser is a method that takes in first name, last_name, username, email, and password as parameters.
    # It creates and saves a SuperUser with the given parameters.
    def create_superuser(self, first_name, last_name, username, email, password=None):
        # Create a user using the create_user method
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password
        )

        # Set the admin-related flags to True
        user.is_active = True
        user.is_staff = True
        user.is_admin = True
        user.is_superadmin = True
        # Save the user object into the database
        user.save(using=self._db)
        return user

# User is a class that extends AbstractUser. It represents a user in the system.
class User(AbstractUser):
    # Define constants for user roles
    RESTURANT = 1
    CUSTOMER = 2

    # Define choices for user roles
    ROLE_CHOICE = (
        (RESTURANT, 'Restaurant'),
        (CUSTOMER, 'Customer')
    )

    # Define fields for the User model
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # Define required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # Define the field that will be used as username field
    USERNAME_FIELD = 'email'
    # Define the fields that will be prompted when creating a superuser
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    # Set the manager for the User model
    objects =  UserManager()

    # Return a string representation of the User object
    def __str__(self):
        return self.email

    # Check if user has a specific permission
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Check if user has permissions for a specific app
    def has_module_perms(self, app_label):
        return True

# UserProfile is a class that represents a user's profile in the system.
# This class has a One to One relationship with the User model.
# This class is used to store additional information about a user.
class UserProfile(models.Model):
    # Define fields for the UserProfile model
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True) # One to One relationship with User model
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photos', blank=True, null=True)
    address_line_1 = models.CharField(max_length=50, blank=True, null=True)
    address_line_2 = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=15, blank=True, null=True)
    state = models.CharField(max_length=15, blank=True, null=True)
    city = models.CharField(max_length=15, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.FloatField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Return a string representation of the UserProfile object
    def __str__(self):
        return self.user.email