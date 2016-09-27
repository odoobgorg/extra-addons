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
                'product_price_taxes_included',
                'product_pricelist',
                'product_prices_update',
                'product',
                'product_visible_discount',
                'product_category_full_name_search',
                'sale_report_hide_price',
                'sale_cancel_reason',
                'sale_crm',
                'sale_report_hide_price',
                'product_expiry',
                'product_manufacturer',
                'product_multi_category',
                'product_multi_link',
                'product_tags',
                'product_warranty',
                'product_website_categ_search',
                'website_sale_options',
                'payment_paypal',
                'base_iban',
                'base_vat',
                'decimal_precision',
                'link_tracker',
                'website_livechat',
                'website_blog',
                'website_blog_mgmt',
                'snippet_google_map',
                'snippet_latest_posts',
                'website_animate',
                'website_google_map',
                'website_portal_sale',
                'website_sale',
                'website_sale_options',
                'website_sale_stock',
                'website_crm',
                'website_customer',
                'website_quote',
                'html_form_builder_snippets'
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
