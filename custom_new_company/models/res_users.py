# -*- coding: utf-8 -*-

from odoo import models, api


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def _signup_create_user(self, values):
        # Create new company on sign up with defined oauth provider
        provider = self.env['ir.config_parameter'].sudo().get_param('auth_signup.company_on_provider.provider_id')
        print("provider : ",provider, "=>", "oauth_uid : ", values['oauth_uid'], "oauth_provider_id : ", values['oauth_provider_id'])
        if values['oauth_uid'] and values['oauth_provider_id'] == provider:
            company = self.env['res.company'].create({'name': values['name']})
            values['company_id'] = company.id
            values['company_ids'] = [(4, company.id)]
        new_user = super(ResUsers, self)._signup_create_user(values)
        return new_user
