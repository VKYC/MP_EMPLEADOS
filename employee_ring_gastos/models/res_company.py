import re

from odoo import api, fields, models, SUPERUSER_ID
from odoo.tools.translate import _


class ResCompany(models.Model):
    _inherit = "res.company"

    account_active = fields.Many2one(
        "account.account",
        string="Cuenta Activa",
        domain="[('user_type_id', '=', 15)]",
    )
    account_passive = fields.Many2one(
        "account.account",
        string="Cuenta Pasiva",
        domain="[('user_type_id', '=', 13)]",
    )

    # account_id = fields.Many2one(
    #     "account.account",
    #     string="Cuenta Activa",
    # )
    # second_currency_id = fields.Many2one(
    #     "account.account",
    #     string="Cuenta Activa",
    # )
    # intercompany_user_id = fields.Many2one("account.account", string="Create as",
    #                                        help="Responsible user for creation of documents triggered by intercompany rules.")
