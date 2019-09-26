# -*- coding: utf-8 -*-
{
    'name': "Report invoice test",

    'summary': """
        Test invoice report
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account'],

    # always loaded
    'data': [
        'data/paperformat.xml',
        'report/reports.xml',
        'report/account_voice_report.xml',
    ],
    'installable': True,
    'application': True,
}