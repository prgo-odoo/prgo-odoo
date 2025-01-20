# -*- coding: utf-8 -*-
{
    'name': "urban_iki_sale",

    'summary': "",

    'description': """
Long description of module's purpose
    """,

    'author': "Odoo PS",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',

    'version': '17.0.3.0.3',

    # any module necessary for this one to work correctly
    'depends': ['sale_management', 'stock_delivery', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',

        'views/account_report.xml',

        'views/res_partner_views.xml',
        'views/ir_qweb_widget_templates.xml',
        'views/report_invoice.xml',
        'views/account_move_line_views.xml',
        'report/report_deliveryslip.xml',
        'report/report_sale_order.xml',
    ],
    'license': 'LGPL-3',
}

