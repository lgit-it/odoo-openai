from odoo import models, fields, api


class GptModel(models.Model):
    _name = "gpt_model"
    _description = "Gpt Model"

    name = fields.Char()
    active = fields.Boolean(string='Active', default=True)
    description  = fields.Char(string='')
    code= fields.Char(string='')
    
    