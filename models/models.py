# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class arch(models.Model):
#     _name = 'arch.arch'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Arch(models.Model):
    _name = 'arch.task'
    _inherit = 'mail.thread'
    _description = 'This is the main model for the module'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    def do_clear_done(self):
        domain = [('is_done', '=', True), '|', ('user_id', '=', self.env.uid), ('user_id', '=', 'False')]
        dones = self.search(domain)
        if dones:
            dones.write({'active': False})
        return True
