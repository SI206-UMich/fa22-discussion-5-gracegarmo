import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in sentence:
		if i == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		maxStock = self.items[0].stock
		maxItem = self.items[0]
		for item in self.items[1:]:
			if item.stock > maxStock:
				maxItem = item
				maxStock = item.stock

		return maxItem
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		maxPrice = self.items[0].price
		maxItem = self.items[0]
		for item in self.items[1:]:
			if item.price > maxPrice:
				maxItem = item
				maxPrice = item.price

		return maxPrice



# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		self.assertEqual(count_a("apples are deliciosa"),3,"count_a(apples are deliciosa)")
		self.assertEqual(count_a("sentence"),0,"count_a(sentence)")
		self.assertEqual(count_a("aaaa"),4,"count_a(sentence)")
		self.assertEqual(count_a("this sentence has 2 as"),2,"count_a(sentence)")

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.warehouse = Warehouse()
		self.warehouse.add_item(self.item1)
		self.assertEqual(len(self.warehouse.items),1,"testing adding an item")


	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		pass


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		pass
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()