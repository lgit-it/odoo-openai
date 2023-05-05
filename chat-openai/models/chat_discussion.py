from odoo import models, fields, api

class ChatDiscussion(models.Model):
    _name = 'chat_discussion'
    _description = 'Chat Discussion'

    name = fields.Char()
    active = fields.Boolean(string='Active', default=True)
    user_id = fields.Many2one('res.users', string='User')
    prompt = fields.Text(string='Prompt')
    chat_folder_type_id = fields.Many2one('chat_folder', string='Chat Folder')
    gpt_model_id = fields.Many2one('gpt_model', string='GPT Model')
    token_limit = fields.Integer(string='Max Token', default="4000")
    max_lenght = fields.Integer(string='Max Lenght',default="12000")
    token_used = fields.Integer(string='Token Used', default= 0 )
    time_start = fields.Datetime(string='Time Start')
    