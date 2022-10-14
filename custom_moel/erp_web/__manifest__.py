{
    'name':'Tester ERP',
    'version': '1.0.0',
    'category': 'ERP',
    'summary': 'Tester Website ERP',
    'description': """ This is website test ERP for VMTS """,
    'sequence':-100,
    'depends':[],
    'data':[
        'security/ir.model.access.csv',
        'view/menu.xml',
        'view/patient_view.xml'
    ],
    'demo':[],
    'application' : True,
    'auto-install' : False,
    'license':'LGPL-3',
}