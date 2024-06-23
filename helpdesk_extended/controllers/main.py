from odoo import http
from odoo.http import request
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController

class HelpdeskCategorySugController(http.Controller):
    @http.route('/category_suggest', auth='user', website=True)
    def category_suggest(self, **kw):
        return request.render("helpdesk_extended.suggest", {})
    
    @http.route('/category_suggest/send', methods=['POST'], auth='user', website=True)
    def send_category_suggest(self, **kw):
        request.env['helpdesk.category.sug'].sudo().create({
            'category_name': kw.get('suggestion'),
            'description': kw.get('description'),
            'user_id': request.env.user.id,
            'user_email': request.env.user.email
        })
        return request.render("helpdesk_extended.suggestion_sended", {})
    
class ExtendedHelpdeskTicketController(HelpdeskTicketController):

    def create_new_ticket(self, **kw):
        # checks if the user has already tried to submit a ticket with a short description, assigns true to desc_err, and removes 'desc_err' from the session
        descr_err = request.session.pop('descr_err', None)
        res = super(ExtendedHelpdeskTicketController, self).create_new_ticket(**kw)
        if descr_err:
            res.qcontext['descr_err'] = descr_err
        return res
    
    def submit_ticket(self, **kw):
        # Return an error if the description is lower than 25 characters
        if len(kw.get("description")) <= 15:
            # Save error message in session
            request.session['descr_err'] = True
            return request.redirect("/new/ticket")
        res = super(ExtendedHelpdeskTicketController, self).submit_ticket(**kw)
        return res