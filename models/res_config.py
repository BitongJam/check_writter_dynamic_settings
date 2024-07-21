from odoo import _, api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
   
    yy_date_pos = fields.Float(help="Check date Year Position")
    mm_date_pos = fields.Float(help="Check date Month Position")
    dd_date_pos = fields.Float(help="Check date Day Position")
    payor_pos = fields.Float(help="Check Payor Position")
    amnt_pos = fields.Float(help="Check Amount Position")
    amnt_word_pos = fields.Float(help="Check Amount in Words Position")
   
    def set_values(self):
        """employee setting field values"""
        res = super(ResConfigSettings, self).set_values()  
        self.env['ir.config_parameter'].set_param('check_writter_dynamic_settings.yy_date_pos', self.yy_date_pos)
        self.env['ir.config_parameter'].set_param('check_writter_dynamic_settings.mm_date_pos', self.mm_date_pos)
        self.env['ir.config_parameter'].set_param('check_writter_dynamic_settings.dd_date_pos', self.dd_date_pos)
        self.env['ir.config_parameter'].set_param('check_writter_dynamic_settings.payor_pos', self.payor_pos)
        self.env['ir.config_parameter'].set_param('check_writter_dynamic_settings.amnt_pos', self.amnt_pos)
        self.env['ir.config_parameter'].set_param('check_writter_dynamic_settings.amnt_word_pos', self.amnt_word_pos)
        return res
   
    def get_values(self):
        """employee limit getting field values"""
        res = super(ResConfigSettings, self).get_values()
        v_yy_date_pos = self.env['ir.config_parameter'].sudo().get_param('check_writter_dynamic_settings.yy_date_pos')
        v_mm_date_pos = self.env['ir.config_parameter'].sudo().get_param('check_writter_dynamic_settings.mm_date_pos')
        v_dd_date_pos = self.env['ir.config_parameter'].sudo().get_param('check_writter_dynamic_settings.dd_date_pos')
        v_payor_pos = self.env['ir.config_parameter'].sudo().get_param('check_writter_dynamic_settings.payor_pos')
        v_amnt_pos = self.env['ir.config_parameter'].sudo().get_param('check_writter_dynamic_settings.amnt_pos')
        v_amnt_word_pos = self.env['ir.config_parameter'].sudo().get_param('check_writter_dynamic_settings.amnt_word_pos')     

        res.update(
            yy_date_pos=float(v_yy_date_pos),
            mm_date_pos=float(v_mm_date_pos),
            dd_date_pos=float(v_dd_date_pos),  # Corrected this line
            payor_pos=float(v_payor_pos),
            amnt_pos=float(v_amnt_pos),
            amnt_word_pos=float(v_amnt_word_pos),
        )
        return res
