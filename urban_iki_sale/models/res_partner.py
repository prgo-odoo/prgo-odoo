# -*- coding: utf-8 -*-

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    partner_customer_product_number = fields.One2many('customer.product.number', 'partner_id')
