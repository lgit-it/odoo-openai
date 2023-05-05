from odoo import models, fields, api


class ChatFolder(models.Model):
    _name = "chat_folder"
    _description = "Chat Discussion"

    name = fields.Char()
    active = fields.Boolean(string='Active', default=True)
    
    chat_folder_type = fields.Selection([('private', 'Private'), ('public', 'Public')], string='Chat Type' , default='public')