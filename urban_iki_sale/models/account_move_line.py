# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    customer_product_numbers = fields.Char(compute='_compute_customer_product_numbers', store=True)

    @api.depends('partner_id.partner_customer_product_number', 'partner_id', 'product_id')
    def _compute_customer_product_numbers(self):
        for line in self:
            customer_product_numbers = next(
                (record.number
                    for record in line.partner_id.partner_customer_product_number
                    if record.product_id.id == line.product_id.id
                ),False
            )
            line.customer_product_numbers = customer_product_numbers
