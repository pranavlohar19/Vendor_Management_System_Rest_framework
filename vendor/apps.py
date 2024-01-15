from django.apps import AppConfig


class VendorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor'

    def ready(self):
        import vendor.signals  # Replace with the actual path to your signals module.
        