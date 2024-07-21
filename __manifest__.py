{
    'name': 'Check Writter Dynamic Settings',
    'version': '14.0',
    'description': '''
        Check Writter Dynamic Position Settings
            - All Fields Display in Check Wriiter can be change using configuration
    ''',
    'author': 'James Michael Ortiz',
    'license': 'LGPL-3',
    'depends': [
        'account','base','web'
    ],
    'data':[
        # 'views/check_res_config_set.xml',
        'report/check_writter.xml',
        'report/report.xml',
        'views/res_config.xml',
        'views/menu.xml'
        
    ],
    'auto_install': False,
    'application': False,
}