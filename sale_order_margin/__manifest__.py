# -*- coding: utf-8 -*-
# (c) 2022 Nexta - Carlos Ros <cros@nextads.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/a
{
    "name": "Sale Order Move Margin",
    'summary': """  Este modulo mueve el margen del SO al la pestaña de otra informacion """,
    'description': """    Este modulo mueve el margen del SO al la pestaña de otra informacion    """,
    'author': "NextaDS",
    'website': "https://www.nextads.es",
    'category': 'Uncategorized',
    'version': '15.0.1.8',
    'license': "LGPL-3",
    'depends': [
        'sale_margin',
    ],
    'data': [
        'views/sale_order_inherit_view.xml'
    ],
    'installable': True
}