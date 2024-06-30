import xmlrpc.client
import os


class Connection:
    def __init__(self):
        self.url = os.environ.get("URL")
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
        products = self.models.execute_kw(
            self.db, self.uid, self.key, "product.product", "search_read", [[]]
        )
        return products

    def list_products(self):
        # List products in a formatted string
        products = self.get_products()
        products = sorted(products, key=lambda x: x["name"])
        products_list = ""
        for product in products:
            products_list += f"""*ID: {product['id']}* - Name: {product['display_name']}
        On hand: {product['qty_available']} \n"""
        return products_list
    
    def get_image(self, product_id):
        return "{}/web/image/product.product/{}/image_1024/".format(
            self.url, product_id
        )

    def product_details(self, product_id):
        # Fetch and format product details by ID
        product = self.models.execute_kw(
            self.db, self.uid, self.key, "product.product", "read", [[int(product_id)]]
        )
        return f"""
        Name: {product[0]['display_name']}
        ID: {product[0]['id']}
        Price: {product[0]['list_price']}
        Cost: {product[0]['standard_price']}
        On hand: {product[0]['qty_available']}
        Product Type: {product[0]['detailed_type']}
        Product Category: {product[0]['categ_id'][1]}
        Invoicing Policy: {product[0]['invoice_policy']}
        """


    def adjust_inventory(self, prod_and_qty):
        try:
            # Extract the product id from the user text, which is the first number after the command /adj
            product_id = int(prod_and_qty.split()[0])
            # Extract the quantity of the product, which is the second number after the command /adj
            quantity = prod_and_qty.split()[1]

            # Locate the product in the inventory adjustment model
            adjs = self.models.execute_kw(
                self.db,
                self.uid,
                self.key,
                "stock.quant",
                "search",
                [[("product_id", "=", product_id)]],
            )

            # If the product exists in the model, then the adjustment will be made
            if adjs:
                self.models.execute_kw(
                    self.db,
                    self.uid,
                    self.key,
                    "stock.quant",
                    "write",
                    [[adjs[0]], {"inventory_quantity": float(quantity)}],
                )

                # Locate the product in the product.template to show the difference between the previous and the current quantity
                product = self.models.execute_kw(
                    self.db,
                    self.uid,
                    self.key,
                    "product.product",
                    "read",
                    [[product_id]],
                )

                return f"Difference: {float(quantity) - product[0]['qty_available']}"
            else:
                return "Product doesn't present in adjustment model"
        except Exception:
            return "Error in the message"

