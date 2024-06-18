{
    'name': 'Employee Stock Location',
    'version': '15.0.0.0.2',
    'summary': """ Employee Transit Location Feature """,
    'author': 'HOLDCO Networks - Baruc Alvarez',
    'website': 'HOLDCO Networks',
    'category': 'Employees',
    'depends': ['base', 'stock', 'employee_ring_gastos', 'hr'],
    "data": [
        "views/menu_item_stock_location.xml",
        "views/stock_location_views.xml",
        "views/hr_employee_views.xml"
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
