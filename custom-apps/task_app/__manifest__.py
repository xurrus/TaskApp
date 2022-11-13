# -*- coding: utf-8 -*-
{
    'name': "task_app",

    'summary': """
        Aplication to control different task""",

    'description': """
        This app controls diferent tasks you have to do
    """,

    'author': "Carlos Duato",
    'website': "http://www.isca.es",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/task_view.xml',
        'views/menu.xml',
        'views/category_view.xml',
        'views/menu_category.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
