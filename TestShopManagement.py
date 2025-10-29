import unittest
from shop import shop_management

class TestShopManagement(unittest.TestCase):
    def setUp(self):
        self.shop = shop_management()

    def test_add_new_product(self):
        self.shop.add_product("notebook", 5.0, 2.0, 10)
        self.assertEqual(len(self.shop.products), 1)
        self.assertEqual(self.shop.products[0]["name"], "notebook")
        self.assertEqual(self.shop.products[0]["price"], 5.0)
        self.assertEqual(self.shop.products[0]["profit"], 2.0)
        self.assertEqual(self.shop.products[0]["inventory"], 10)

    def test_add_existing_product_updates_inventory(self):
        self.shop.add_product("pencil", 1.0, 0.3, 20)
        self.shop.add_product("pencil", 1.0, 0.3, 15)
        self.assertEqual(len(self.shop.products), 1)
        self.assertEqual(self.shop.products[0]["inventory"], 35)

    def test_sell_product_reduces_inventory(self):
        self.shop.add_product("eraser", 0.5, 0.1, 50)
        self.shop.sell_product("eraser", 10)
        self.assertEqual(self.shop.products[0]["inventory"], 40)

    def test_sell_product_adds_to_sold_list(self):
        self.shop.add_product("ruler", 2.0, 0.5, 30)
        self.shop.sell_product("ruler", 5)
        self.assertEqual(len(self.shop.sold), 1)
        self.assertEqual(self.shop.sold[0]["name"], "ruler")
        self.assertEqual(self.shop.sold[0]["How_many"], 5)

    def test_sell_product_updates_existing_sold_entry(self):
        self.shop.add_product("pen", 1.5, 0.4, 100)
        self.shop.sell_product("pen", 10)
        self.shop.sell_product("pen", 15)
        self.assertEqual(len(self.shop.sold), 1)
        self.assertEqual(self.shop.sold[0]["How_many"], 25)

    def test_cannot_sell_more_than_inventory(self):
        self.shop.add_product("marker", 3.0, 1.0, 5)
        self.shop.sell_product("marker", 8)
        self.assertEqual(self.shop.products[0]["inventory"], 5)

    def test_inventory_check_existing_product(self):
        self.shop.add_product("stapler", 8.0, 2.0, 12)
        self.shop.inventory("stapler")

    def test_inventory_check_nonexistent_product(self):
        self.shop.inventory("glue")

    def test_low_inventory_alert(self):
        self.shop.add_product("clip", 0.2, 0.05, 2)
        self.shop.sell_product("clip", 1)

    def test_report_of_the_day_calculations(self):
        self.shop.add_product("book", 10.0, 3.0, 20)
        self.shop.add_product("calculator", 15.0, 5.0, 10)
        self.shop.sell_product("book", 3)
        self.shop.sell_product("calculator", 2)
        self.shop.Report_of_the_day()

    def test_the_product_of_day_identification(self):
        self.shop.add_product("paper", 2.0, 0.6, 100)
        self.shop.add_product("folder", 4.0, 1.2, 50)
        self.shop.sell_product("paper", 25)
        self.shop.sell_product("folder", 30)
        self.shop.sell_product("paper", 15)
        self.shop.the_product_of_day()

    def test_complete_business_workflow(self):
        self.shop.add_product("notebook", 5.0, 2.0, 50)
        self.shop.add_product("pen", 1.5, 0.4, 100)
        self.shop.sell_product("notebook", 10)
        self.shop.sell_product("pen", 25)
        self.shop.sell_product("notebook", 5)
        self.shop.sell_product("pen", 15)
        self.assertEqual(self.shop.products[0]["inventory"], 35)
        self.assertEqual(self.shop.products[1]["inventory"], 60)
        self.assertEqual(len(self.shop.sold), 2)
        self.shop.Report_of_the_day()
        self.shop.the_product_of_day()

    def test_sell_product_with_zero_quantity(self):
        self.shop.add_product("pencil", 1.0, 0.3, 20)
        self.shop.sell_product("pencil", 0)
        self.assertEqual(self.shop.products[0]["inventory"], 20)

    def test_multiple_products_same_name_different_objects(self):
        self.shop.add_product("notebook", 5.0, 2.0, 10)
        self.shop.add_product("notebook", 6.0, 2.5, 15)
        self.assertEqual(len(self.shop.products), 1)
        self.assertEqual(self.shop.products[0]["inventory"], 25)


if __name__ == "__main__":
    unittest.main()
