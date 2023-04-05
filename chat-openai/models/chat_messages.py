from odoo import models, fields, api

class ChatMessage(models.Model):
    _name = 'chat_message'
    _description = 'Chat Message'

    name = fields.Char()
    active = fields.Boolean(string='Active', default=True)
    
    chat_discussion_id = fields.Many2one('chat_discussion', string='Chat Discussion')

    _sequence = fields.Integer(string='Sequence')

    user_id = fields.Many2one('res.users', string='User')
    role = fields.Char(string='Role')
    content= fields.Text(string='Content')
    token_used = fields.Integer(string='Token Used', default= 0 )
    time_start = fields.Datetime(string='Time Start')
    


class ChatDiscussion (models.Model):
    _inherit = 'chat_discussion'

    chat_message_ids = fields.One2many('chat_message', 'chat_discussion_id', string='Chat Messages')
    last_time = fields.Datetime(string='Last Time', 
        compute='_compute_last_time', store=True, readonly=True)
    
    
    @api.depends('depends')
    def _compute_last_time(self):
        for record in self:
            record.field = something
    
    
    )