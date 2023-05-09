# -*- coding: utf-8 -*-
{
    'name': "chat-openai",

    'summary': """
        An interface to use custom openai chat in odoo""",

    'description': """
       Chat-Openai use openai api to create a chatbot in odoo
    """,

    'author': "LGIT",
    'website': "http://lgit.it",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/gpt_model_views.xml',
        "views/chat_discussion_views.xml",
        "views/chat_message_views.xml",
        "views/chat_folder_views.xml",
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
