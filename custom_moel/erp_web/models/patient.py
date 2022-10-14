from odoo import api,fields,models,_,tools

class WebERPPatient(models.Model):
    _name = "erp.patient"
    _description = "ERP Patient"

    name =fields.Char(string='Name')
    age =fields.Integer(string='Age')
    gender = fields.Selection([('male','Male'),('female','Female')],string="Gender")

