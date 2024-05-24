from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    # This method is used to import signals from the signals.py file
    def ready(self):
        import accounts.signals