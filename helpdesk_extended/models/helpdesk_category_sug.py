from odoo import models, fields, api

class HelpCategorySug(models.Model):
    _name = "helpdesk.category.sug"
    
    category_name = fields.Char("Category Name", readonly=True)
    description = fields.Text("Category Description", readonly=True)
    user_id = fields.Many2one("res.users", string="User", readonly=True)
    editable = fields.Boolean("Editable", readonly=True, default=False)
    added_to_categories = fields.Boolean("Added to categories", readonly=True)
    user_tickets_ids = fields.One2many("helpdesk.ticket", inverse_name="suggestion_id", compute="_compute_user_tickets")
    user_email = fields.Char("User email")
    
    
    def add_category(self):
        new_category = self.env['helpdesk.ticket.category'].create({
            'name': self.category_name,
        })
        self.added_to_categories = True
        return new_category
    
    def change_to_editable(self):
        self.editable = True
        
    def change_to_non_editable(self):
        self.editable = False
        
    @api.model
    def _compute_user_tickets(self):
        for rec in self:
            if rec.user_id:
                user_tickets = self.env['helpdesk.ticket'].search([('partner_id.email', '=', rec.user_email)])
                rec.user_tickets_ids = user_tickets

    @api.depends("category_name", "added_to_categories")
    def _compute_display_name(self):
        for rec in self:
            if rec.added_to_categories:
                rec.display_name = f"{rec.category_name} - Accepted"
            else:
                rec.display_name = f"{rec.category_name} - Suggested"