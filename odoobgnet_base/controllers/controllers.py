# -*- coding: utf-8 -*-
from openerp import http

# class OdoobgorgBase(http.Controller):
#     @http.route('/odoobgorg_base/odoobgorg_base/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoobgorg_base/odoobgorg_base/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoobgorg_base.listing', {
#             'root': '/odoobgorg_base/odoobgorg_base',
#             'objects': http.request.env['odoobgorg_base.odoobgorg_base'].search([]),
#         })

#     @http.route('/odoobgorg_base/odoobgorg_base/objects/<model("odoobgorg_base.odoobgorg_base"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoobgorg_base.object', {
#             'object': obj
#         })