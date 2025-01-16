# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = "stock.move"

    customer_product_numbers = fields.Char(compute='_compute_customer_product_numbers', store=True)

    @api.depends('picking_id.sale_id.partner_id.partner_customer_product_number', 'picking_id.sale_id.partner_id', 'product_id')
    def _compute_customer_product_numbers(self):
        for move in self:
            partner = move.picking_id.sale_id.partner_id
            customer_product_numbers = next(
                (record.number
                    for record in partner.partner_customer_product_number
                    if record.product_id.id == move.product_id.id
                ),False
            )
            move.customer_product_numbers = customer_product_numbers


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    def _get_aggregated_product_quantities(self, **kwargs):
        """Returns dictionary of products and corresponding values of interest + customer product code + weight
        """
        aggregated_move_lines = super()._get_aggregated_product_quantities(**kwargs)
        for aggregated_move_line in aggregated_move_lines:
            customer_product_code = aggregated_move_lines[aggregated_move_line]['move'].customer_product_numbers
            weight = aggregated_move_lines[aggregated_move_line]['product'].weight
            weight_uom_name = aggregated_move_lines[aggregated_move_line]['product'].weight_uom_name
            default_code = aggregated_move_lines[aggregated_move_line]['product'].default_code
            aggregated_move_lines[aggregated_move_line]['customer_product_numbers'] = customer_product_code
            aggregated_move_lines[aggregated_move_line]['weight'] = weight
            aggregated_move_lines[aggregated_move_line]['weight_uom_name'] = weight_uom_name
            aggregated_move_lines[aggregated_move_line]['default_code'] = default_code
        return aggregated_move_lines
