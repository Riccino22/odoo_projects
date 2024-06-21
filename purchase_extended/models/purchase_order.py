from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    can_delete_after = fields.Datetime("Can delete after")
    visible_order = fields.Boolean("Visible order")
    order_url = fields.Char("URL", compute="_compute_url")

    def _check_order_lines(self):
        for order in self:
            if not order.order_line:
                # Raise a validation error if the order has no order lines
                raise ValidationError("The order must have elements in order lines")

    @api.onchange("state")
    def _modify_visible_order(self):
        for order in self:
            if order.state != "purchase":
                order.visible_order = False
                
    @api.onchange("visible_order", "state")
    def _compute_url(self):
        for order in self:
            if order.visible_order:
                order.order_url = (
                    f"http://localhost:8069/purchase_order/{order.id}".replace(
                        "NewId_", ""
                    )
                )
            else:
                order.order_url = ""

    @api.model_create_multi
    def create(self, vals_list):
        orders = super(PurchaseOrder, self).create(vals_list)
        # Ensure the newly created orders have order lines
        orders._check_order_lines()
        return orders

    @api.ondelete(at_uninstall=False)
    def _delete_order_after_date(self):
        for order in self:
            # Prevent deletion if the current time is before the can_delete_after date
            if (
                order.can_delete_after
                and order.can_delete_after > fields.Datetime.now()
            ):
                raise ValidationError(
                    f"You can not delete this record before {order.can_delete_after}. If you want delete it, empty the can_delete_after field, save and try to delete"
                )

    def write(self, vals):
        orders = super(PurchaseOrder, self).write(vals)
        # Update visible_order to False if the state changes to anything other than "purchase"
        if "state" in vals and vals["state"] != "purchase":
            self.write({"visible_order": False})
        # Ensure the updated orders have order lines    
        self._check_order_lines()
        return orders
