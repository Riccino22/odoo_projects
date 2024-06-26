import xmlrpc.client
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


class Connection:
    def __init__(self):
        # Initialize connection parameters
        self.url = "http://localhost:8069"
        self.db = "odoo16db"
        self.username = "riccino"
        self.key = os.environ.get("ODOO_API_KEY")

    def start(self):
        # Create proxies and authenticate
        self.common = xmlrpc.client.ServerProxy("{}/xmlrpc/2/common".format(self.url))
        self.uid = self.common.authenticate(self.db, self.username, self.key, {})
        self.models = xmlrpc.client.ServerProxy("{}/xmlrpc/2/object".format(self.url))

    def get_products(self):
        # Fetch all products
        self.products = self.models.execute_kw(
            self.db, self.uid, self.key, "product.template", "search_read", [[]]
        )
        return self.products

    def list_products(self):
        # List products in a formatted string
        products = self.get_products()
        products_list = ""
        for product in products:
            products_list += f"Name: {product['name']} - ID: {product['id']} - Price: {product['list_price']} \n"
        return products_list

    def product_details(self, product_id):
        # Fetch and format product details by ID
        product = self.models.execute_kw(
            self.db, self.uid, self.key, "product.template", "read", [[int(product_id)]]
        )
        print(product)
        return f"""
        Name: {product[0]['name']}
        ID: {product[0]['id']}
        Price: {product[0]['list_price']}
        Cost: {product[0]['standard_price']}
        Product Type: {product[0]['detailed_type']}
        On hand: {product[0]['qty_available']}
        """
