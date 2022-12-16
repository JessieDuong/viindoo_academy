# -*- coding: utf-8 -*-
{
    'name': "viindoo_academy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Academy',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/academy_security.xml',
        
        'views/root_menu.xml',
        'views/education_class_view.xml',
        'views/education_student_view.xml',
        'views/ethnic.xml',
        'views/academy_enrollment.xml',
        'views/education_class_view_two.xml',
        'views/templates.xml',
        
        'wizards/academy_enrollment_wizard.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
