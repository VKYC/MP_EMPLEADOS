from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    location_id = fields.Many2one(comodel_name='stock.location', string='Transit Location')
    is_transit_location = fields.Boolean(string='Is Transit Location', default=False, copy=False)

    @api.model
    def create(self, vals):
        employee_id = super(HrEmployee, self).create(vals)
        if vals['is_transit_location'] and not vals['location_id']:
            vals['location_id'] = self.env['stock.location'].create({
                'name': vals['identification_id'] + '-' + vals['name'],
                'usage': 'transit',
                'is_employee': True,
                'employee_id': employee_id.id,
            })
        return employee_id

    @api.onchange(is_transit_location)
    def create_transit_location_relation(self):
        for employee_id in self:
            if employee_id.is_transit_location and not employee_id.location_id:
                print('ok')

