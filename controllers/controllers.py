# -*- coding: utf-8 -*-
# from odoo import http


# class Dyjhor(http.Controller):
#     @http.route('/dyjhor/dyjhor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dyjhor/dyjhor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('dyjhor.listing', {
#             'root': '/dyjhor/dyjhor',
#             'objects': http.request.env['dyjhor.dyjhor'].search([]),
#         })

#     @http.route('/dyjhor/dyjhor/objects/<model("dyjhor.dyjhor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dyjhor.object', {
#             'object': obj
#         })
