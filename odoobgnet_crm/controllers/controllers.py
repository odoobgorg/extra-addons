# -*- coding: utf-8 -*-
from openerp import http

# class OdoobgorgEcommerce(http.Controller):
#     @http.route('/odoobgorg_ecommerce/odoobgorg_ecommerce/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoobgorg_ecommerce/odoobgorg_ecommerce/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoobgorg_ecommerce.listing', {
#             'root': '/odoobgorg_ecommerce/odoobgorg_ecommerce',
#             'objects': http.request.env['odoobgorg_ecommerce.odoobgorg_ecommerce'].search([]),
#         })

#     @http.route('/odoobgorg_ecommerce/odoobgorg_ecommerce/objects/<model("odoobgorg_ecommerce.odoobgorg_ecommerce"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoobgorg_ecommerce.object', {
#             'object': obj
#         })