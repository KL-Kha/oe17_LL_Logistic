# -*- coding: utf-8 -*-
{
    "name": "LL Sales",
    "category": "Sales",
    "summary": "",
    "version": "17.0.0.1",
    'author': "",
    'website': "",
    "license": "OPL-1",
    "depends": [
        'base',
        'base_automation',
        'utm',
        'mail'
    ],
    "data": [
        #1 security
        "security/ir.model.access.csv",
        #2 data

        #3 view
        "views/sale_order.xml",

        #4 wizard
        "wizards/send_quotation.xml",
    ],
    "application": True,
    "installable": True,
    "auto_install": False,
}
