{
    'name': 'Employee Stock Location',
    'version': '15.0.0.0.1',
    'summary': """ Employee Transit Location Feature """,
    'author': 'Baruc Álvarez',
    'category': 'Employees',
    'depends': ['base', 'stock', 'employee_ring_gastos'],
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
