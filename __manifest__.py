# -*- coding: utf-8 -*-
{
    'name': 'SD Times',
    'version': '18.0.1.0.0',
    'description': '',
    'category': 'Services',
    'summary': """ Employees timesheet """,
    'author': 'Arash Homayounfar',
    'company': 'Giladoo',
    'maintainer': 'Giladoo',
    'website': "https://www.giladoo.com/times",
    'installable': True,
    'auto_install': False,
    'application': True,
    'depends': ['base', 'web', 'sd_projects'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',

    ],
    'assets':{
        'web.assets_backend':[
          # 'sd_hr/static/src/components/**/*',
        ],
    },

    'license': 'LGPL-3',
}
