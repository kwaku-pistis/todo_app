# -*- coding: utf-8 -*-
{
    'name': "arch",

    'summary': """
        This is a trial module or my first module.
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "pistis",
    'website': "http://www.pistis.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/arch_menu.xml',
        'views/arch_todo_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}