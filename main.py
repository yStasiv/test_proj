"""Store gods and set name related to actual count"""


class Enum:
    MILK = "milk"
    CHEESE = "cheese"


class Item:
    """Prepare item data (name, end_date, supplier_name)"""

    def __init__(self, name: str, end_date: str, supplier: str):
        self.name = name
        self.end_date = end_date
        self.supplier = supplier


class Warehouse:
    """Clas contain actual gods"""

    def __init__(self):
        self.milk_list: list = []
        self.cheese_list: list = []

    def store_gods(self, list_of_gods) -> None:
        """Check naming and sort to lists"""
        # Use if else as we have just two different cases milk or cheese
        for item in list_of_gods:
            self.milk_list.append(item) if Enum.MILK in item.name else self.cheese_list.append(item)

    def add_new_item(self, item: Item):
        """Detect name and update actual data"""
        # Update item name
        item.name = f"{item.name}{len(self.milk_list if Enum.MILK in item.name else self.cheese_list) + 1}"
        # Update list
        self.milk_list.append(item) if Enum.MILK in item.name else self.cheese_list.append(item)

    def get_latest_warehouse_data(self):
        """Return all stored gods"""
        for_easy_reading = []
        for item in (self.milk_list + self.cheese_list):
            for_easy_reading.append(f"name: {item.name}, end date: {item.end_date}, suppler name: {item.supplier}")

        return for_easy_reading


if __name__ == '__main__':
    # Set gods
    goods = [
        Item(name="milk1", end_date="2020-20-20", supplier="Yurii"),
        Item(name="milk2", end_date="2021-20-20", supplier="Yurii"),
        Item(name="cheese1", end_date="2022-20-20", supplier="Nick"),
    ]

    # Init class
    warehouse = Warehouse()
    # Add actual gods to warehouse
    warehouse.store_gods(goods)

    # Add new positions
    warehouse.add_new_item(Item(name=Enum.CHEESE, end_date="2024-20-20", supplier="Den"))
    warehouse.add_new_item(Item(name=Enum.MILK, end_date="2027-20-20", supplier="Yurii"))
    warehouse.add_new_item(Item(name=Enum.CHEESE, end_date="2027-20-20", supplier="New Yurii"))

    # Return updated list of gods
    print(warehouse.get_latest_warehouse_data())
