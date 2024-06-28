from odoo import models, fields, api
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()


class GeneratePriceProduct(models.TransientModel):
    _name = "inventory_extended.gen_price"
    _description = "Wizard for generate prices"

    product_id = fields.Many2one("product.template", string="Product", required=True)
    price = fields.Float("Price", compute="_compute_price")

    @api.depends("product_id")
    def _compute_price(self):
        for record in self:                
            if record.product_id:
                # Initialize the language model and define the messages
                llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

                messages = [
                    SystemMessage(
                        content="You are a great vendor with abilities to determine prices for products"
                    ),
                    HumanMessage(
                        content="""
                    State as precisely as you can, what is the price of the following product:
                    * {}.
                    Respond to me with a price for this product, using your criteria to evaluate product prices.

                    Respond to me only with the price you assigned to this product. Your response should follow the following structure:

                    price: (the price you chose) $
                    """.format(
                            record.product_id.name
                        )
                    ),
                ]

                # Invoke the language model
                output = llm.invoke(messages)
                price = output.content

                # Process the output to extract the price
                price = price.replace(",", "").replace("price:", "").replace("$", "")
                record.price = float(price.split()[0])

    def update_price(self):
        self.price
        for record in self:
            product = self.env["product.template"].search(
                [("id", "=", record.product_id.id)]
            )
            product.write({"list_price": record.price})
