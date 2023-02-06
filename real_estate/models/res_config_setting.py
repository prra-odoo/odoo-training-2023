from odoo import api,fields,models

class ResConfigSettings(models.TransientModel):
    
    _inherit = "res.congig.setting"
    
    navbar_bg_color = fields.Char()
    navbar_text_color = fields.Char()
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettings,self).get_values()
        IPC = self.env['ir.config_parameter'].sudo()
        
        navbar_bg_color = IPC.get_param('change_odoo_theme_header_color.navbar_bg_color')
        navbar_text_color = IPC.get_param('change_odoo_theme_header_color.navbar_text_color')
        
        res.update(
            navbar_background_color=navbar_bg_color,
            navbar_text_color=navbar_text_color,
        )
        return res
    
    def set_values(self):
        super(ResConfigSettings, self).set_values()
        IPC = self.env['ir.config_parameter'].sudo()
        IPC.set_param('change_odoo_theme_header_color.navbar_bg_color',self.navbar_bg_color)
        IPC.set_param('change_odoo_theme_header_color.navbar_text_color',self.navbar_text_color)
    