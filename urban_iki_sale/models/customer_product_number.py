# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomerProductNumber(models.Model):
    _name = 'customer.product.number'
    _description = 'customer_product_number'

    partner_id = fields.Many2one(comodel_name='res.partner', string='Partner')
    product_id = fields.Many2one('product.product', string='Product')
    number = fields.Char('Number')
