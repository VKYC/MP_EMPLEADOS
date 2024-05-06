# -*- coding: utf-8 -*-
{
    'name': 'Employee stock location',
    'version': '15.1',
    'description': """ Employee stock location """,
    'summary': """  """,
    'author': 'Breithner Aquituari',
    'website': '',
    'category': '',
    'depends': [
        'base',
        'stock',
        'employee_ring_gastos' 
        ],
    "data": [
        "views/hr_employee_views.xml",
        "views/menu_item_stock_location.xml",
        "views/stock_location_views.xml"
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
