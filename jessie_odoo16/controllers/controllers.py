# -*- coding: utf-8 -*-
# from odoo import http


# class JessieOdoo16(http.Controller):
#     @http.route('/jessie_odoo16/jessie_odoo16', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jessie_odoo16/jessie_odoo16/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jessie_odoo16.listing', {
#             'root': '/jessie_odoo16/jessie_odoo16',
#             'objects': http.request.env['jessie_odoo16.jessie_odoo16'].search([]),
#         })

#     @http.route('/jessie_odoo16/jessie_odoo16/objects/<model("jessie_odoo16.jessie_odoo16"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jessie_odoo16.object', {
#             'object': obj
#         })
