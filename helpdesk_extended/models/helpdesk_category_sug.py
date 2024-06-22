from odoo import models, fields, api

class HelpCategorySug(models.Model):
    _name = "helpdesk.category.sug"
    
    category_name = fields.Char("Category Name", readonly=True)
    description = fields.Text("Category Description", readonly=True)
    user_id = fields.Many2one("res.users", string="User", readonly=True)
    editable = fields.Boolean("Editable", readonly=True, default=False)
    added = fields.Boolean("Added to categories", readonly=True)
    
    
    def add_category(self):
        new_category = self.env['helpdesk.ticket.category'].create({
            'name': self.category_name,
        })
        self.added = True
        return new_category
    
    def change_to_editable(self):
        self.editable = True
        
    def change_to_non_editable(self):
        self.editable = False