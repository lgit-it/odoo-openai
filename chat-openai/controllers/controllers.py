# -*- coding: utf-8 -*-
# from odoo import http


# class Chat-openai(http.Controller):
#     @http.route('/chat-openai/chat-openai/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chat-openai/chat-openai/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chat-openai.listing', {
#             'root': '/chat-openai/chat-openai',
#             'objects': http.request.env['chat-openai.chat-openai'].search([]),
#         })

#     @http.route('/chat-openai/chat-openai/objects/<model("chat-openai.chat-openai"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chat-openai.object', {
#             'object': obj
#         })
