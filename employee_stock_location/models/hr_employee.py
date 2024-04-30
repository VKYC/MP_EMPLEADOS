# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'


    def _compute_location_ids(self):
        list_transit = []
        exist_values = []
        stock_location = self.env['stock.location'].search([('usage', '=', 'transit')])
        
        for sl in stock_location:
            list_transit.append([sl.id,sl.name])

        for lt in list_transit:
            name_value = (lt[1].replace('-','')).replace(' ', '')
            if self.identification_id:
                if ('%s%s') %(((self.identification_id).replace('-', '')).replace(' ', ''),(self.name).replace(' ', '')) == name_value:
                    exist_values.append(lt[0])
            
        for rec in self:
            rec.location_ids = exist_values


    location_ids = fields.Many2many(
        'stock.location',
        'stock_location_hr_employee_rel',
        'hr_employee_id',
        'stock_location_id',
        compute = _compute_location_ids
    )



