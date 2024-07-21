from odoo import _, api, fields, models



class AccountPayment(models.Model):
    _inherit = 'account.payment'


    conf_yy_check_pos = fields.Float(compute="_compute_set_check_position_conf")
    conf_mm_check_pos = fields.Float(compute="_compute_set_check_position_conf")
    conf_dd_check_pos = fields.Float(compute="_compute_set_check_position_conf")
    conf_payor_check_pos = fields.Float(compute="_compute_set_check_position_conf")
    conf_amnt_check_pos = fields.Float(compute="_compute_set_check_position_conf")
    conf_amnt_wrd_check_pos = fields.Float(compute="_compute_set_check_position_conf")

    
    def _set_check_pos_field(self):
        self.conf_yy_check_pos = False
        self.conf_mm_check_pos = False
        self.conf_dd_check_pos = False
        self.conf_payor_check_pos = False
        self.conf_amnt_check_pos = False
        self.conf_amnt_wrd_check_pos = False
        pass