from odoo import models, fields, api
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()

class GeneratePriceProduct(models.TransientModel):
    _name = "inventory_extended.gen_price"
    _description = "Wizard for generate prices"

    product_id = fields.Many2one("product.template", string="Product")
    details = fields.Text("Product details")
    price = fields.Float("Price", compute="_compute_price")
    #updated = fields.Boolean("Replace product price", default=True, compute="_update_price")
    

    @api.depends("product_id")
    def _compute_price(self):
        for record in self:
            if record.product_id:
                llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")
                messages = [
                    SystemMessage(
                        content="You are a great vendor with habilities for determinate prices for products"
                    ),
                    HumanMessage(
                        content="""
                    State as precisely as you can, what is the price of the following product:
                    * {}.
                    Respond to me with a price for this product, using your criteria to evaluate product prices and information obtained from the Internet.

                    Respond to me only with the price you assigned to this product. Your response should follow the following structure:

                    price: (the price you chose) $
                    """.format(record.product_id.name)
                    ),
                ]

                output = llm.invoke(messages)
                price = output.content
                price = price.replace(",", "").replace("price:", "").replace("$", "")
                record.price = float(price.split()[0])

    #@api.depends_context("updated")
    def update_price(self):
        self.price
        for record in self:
            product = self.env['product.template'].search([('id', '=', record.product_id.id)])
            product.write({'list_price': record.price})
            
            
"""    @api.model_create_multi
    def create(self, vals_list):
        context = dict(self.env.context)
        context['updated'] = True
        for val in vals_list:
            val['price'] = "7"
        return super(GeneratePriceProduct, self.with_context(context)).create(vals_list)
"""
        

"""    @api.depends_context("default_product_id")
    def _compute_price(self):
        res = super()._compute_price(self)
        return res
    """