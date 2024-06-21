from odoo import http
from odoo.http import request

class ManagePurchase(http.Controller):
    @http.route('/purchase_order/<model("purchase.order"):order>', auth='user', website=True)
    def purchase_order(self, order):
        # Render the purchase order template with the given order
        return request.render("purchase_extended.order", {
            'order': order,
        })
