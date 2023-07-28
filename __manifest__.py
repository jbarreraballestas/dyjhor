{
    'name': "Dyjhor",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'installable': True,
    'auto_install': False,
    'application': True,
}
