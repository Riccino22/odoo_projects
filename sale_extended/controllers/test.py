from odoo import http
from odoo.http import request

class TestController(http.Controller):
    @http.route("/sale", auth="public", website=True, type="json")
    def sale_view(self):
        return ""