from django.test import TestCase
from .models import Item

class TestModels(TestCase):
    def test_done_default_to_false(self):
        item = Item.objects.create(name='Test todo Item')
        self.assertFalse(item.done)

    def test_items_string_method_returns_name(self):
            item = Item.objects.create(name='Test todo Item')
            self.assertEqual(str(item), 'Test todo Item')