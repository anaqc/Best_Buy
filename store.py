class Store:
    def __init__(self, list_products: list):
        """ Initialize instance variables"""
        self.list_products = list_products


    def add_product(self, product):
        """ Thia function add a product to list_products"""
        self.list_products.append(product)


    def remove_product(self, product):
        """ This function removes a product from store"""
        try:
            if product in self.list_products:
                self.list_products.remove(product)
            raise ValueError(f"The {product} ist not in store")
        except ValueError as e:
            print(e)


    def get_total_quantity(self) -> int:
        """ This function returns how many items are in the store in total"""
        return len(self.list_products)


    def get_all_products(self) -> list:
        """ This function return all products int the store that are activate"""
        list_products_active = []
        for product in self.list_products:
            if product.active:
                list_products_active.append(product)
        return list_products_active


    def order(self, shopping_list) -> float:
        """
        Gets a list of tuples, where each tuple has 2 items:
        Product (Product class) and quantity (int).
        Buys the products and returns the total price of the order.
        """
        total = 0
        for product, quantity in shopping_list:
            total += product.price * quantity
        return total

