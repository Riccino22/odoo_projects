from odoo.http import request
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController
    
class ExtendedHelpdeskTicketController(HelpdeskTicketController):

    def create_new_ticket(self, **kw):
        res = super(ExtendedHelpdeskTicketController, self).create_new_ticket(**kw)
        # checks if the user has already tried to submit a ticket with a short description, assigns true to desc_err, and removes 'desc_err' from the session
        descr_err = request.session.pop('descr_err', None)
        if descr_err:
            res.qcontext['descr_err'] = descr_err
        return res
    
    def submit_ticket(self, **kw):
        res = super(ExtendedHelpdeskTicketController, self).submit_ticket(**kw)
        # Return an error if the description is lower than 25 characters
        if len(kw.get("description")) <= 15:
            # Save error message in session
            request.session['descr_err'] = True
            return request.redirect("/new/ticket")
        return res