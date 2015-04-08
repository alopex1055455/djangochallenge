from django.test import TestCase
from .models import Events, category

class EventsTestsIfEmpty(TestCase):
    #make sure this is empty
    def test_if_events_empty(self):
        self.assertEqual(len(Events.objects.all()), 0)
    #make sure everything is empty
    def test_if_categories_empty(self):
        self.assertEqual(len(category.objects.all()), 0)

# Create your tests here.
