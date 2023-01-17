# -*- coding:utf-8 -*-

from odoo import models, fields, api


class Account(models.Model):
    _name = "account.property"

    name = fields.Char(requiure= True)
    abc = fields.Char(requiure= True) 
    
