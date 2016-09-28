# -*- coding: utf-8 -*-
{
    'name': "odoobgnet_project",

    'summary': """
        OdooBG.Net Project set of modules""",

    'description': """
        This module is container for the default set of Project Management modules, installed with OdooBG.Net Odoo ERP installation.
    """,

    'author': "OdooBG.Net, Lumnus LTD",
    'website': "http://www.odoobg.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '9.0.1.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': [
                'project',
                'project_kanban',
                'project_team',
                'project_issue',
                'crm_project_issue',
                'project_gantt8',
                'project_issue_sheet',
                'project_timesheet',
                
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
