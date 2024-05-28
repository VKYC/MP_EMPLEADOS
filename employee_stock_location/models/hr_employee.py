from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    location_id = fields.Many2one(comodel_name='stock.location', string='Transit Location')



