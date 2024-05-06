# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    def _compute_location_ids(self):
        stock_location = self.env['stock.location'].search([
            ('employee_id','=', self.id),
            ('usage','=','transit')])

        for rec in self:
            rec.location_ids = stock_location.ids



    location_ids = fields.Many2many(
        'stock.location',
        'stock_location_hr_employee_rel',
        'hr_employee_id',
        'stock_location_id',
        compute = _compute_location_ids,
    )




