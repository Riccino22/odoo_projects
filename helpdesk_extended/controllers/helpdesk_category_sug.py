from odoo import http
from odoo.http import request

class HelpdeskCategorySugController(http.Controller):
    @http.route('/category_suggest', auth='user', website=True)
    def category_suggest(self, **kw):
        return request.render("helpdesk_extended.suggest", {})
    
    @http.route('/category_suggest/send', methods=['POST'], auth='user', website=True)
    def send_category_suggest(self, **kw):
        request.env['helpdesk.category.sug'].sudo().create({
            'category_name': kw.get('suggestion'),
            'description': kw.get('description'),
            'user_id': request.env.user.id
        })
        return request.render("helpdesk_extended.suggestion_sended", {})