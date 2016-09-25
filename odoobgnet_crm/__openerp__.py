# -*- coding: utf-8 -*-
{
    'name': "odoobgnet_ecommerce",

    'summary': """
        OdooBG.Net eCommerce set of modules""",

    'description': """
        This module is container for the default set of modules, automatically installed with each OdooBG.Net eCommerce installation.
    """,

    'author': "OdooBG.Net, Lumnus LTD",
    'website': "http://www.odoobg.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Website',
    'version': '9.0.1.0',
    'license': 'LGPL-3',


    # any module necessary for this one to work correctly
    'depends': [
                
    ],

    # always loaded
    'data': [
    ],
    'sequence': 1,
    'installable': True,
    'auto_install': True,
    'doc': ['doc/index.rst'],
    "application": True,


}