# apps/taxi/apps.py
from django.apps import AppConfig


class TaxiConfig(AppConfig):
    name = 'apps.taxi'

    def ready(self):
        import apps.taxi.signals

