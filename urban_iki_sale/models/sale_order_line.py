# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    customer_product_numbers = fields.Char(compute='_compute_customer_product_numbers', store=True)

    @api.depends('order_partner_id.partner_customer_product_number', 'order_partner_id', 'product_id')
    def _compute_customer_product_numbers(self):
        for line in self:
            customer_product_numbers = next(
                (record.number
                    for record in line.order_partner_id.partner_customer_product_number
                    if record.product_id.id == line.product_id.id
                ),False
            )
            line.customer_product_numbers = customer_product_numbers
