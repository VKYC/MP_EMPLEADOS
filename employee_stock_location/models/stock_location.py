# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class StockLocation(models.Model):
    _inherit = 'stock.location'


    employee_id = fields.Many2one('hr.employee', string="Empleado")
