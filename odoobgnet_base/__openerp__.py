# -*- coding: utf-8 -*-
{
    'name': "odoobgnet_base",

    'summary': """
        OdooBG.Net Default set of modules""",

    'description': """
        This module is container for the default set of modules, automatically installed with each OdooBG.Net installation.
    """,

    'author': "OdooBG.Net, Lumnus LTD",
    'website': "http://www.odoobg.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Technical Settings',
    'version': '9.0.1.0',

    # any module necessary for this one to work correctly
    'depends': [
                'base_technical_features',
                'united_backend_theme',
                'base_setup_enterprise_remove'
                
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    'sequence': 1,
    'installable': True,
    'auto_install': True,
    'doc': ['doc/index.rst'],
    "application": True,


}