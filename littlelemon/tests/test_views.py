from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.item2 = Menu.objects.create(Title="Chicken", Price=830, Inventory=10)
        self.item3 = Menu.objects.create(Title="Feed", Price=60, Inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        for item in items:
            self.assertEqual(item,item)