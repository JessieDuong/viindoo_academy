from odoo import models, fields

class EducationStudentEthnic(models.Model):
    _name="education.student.ethnic"
    _description="Ethnic"
    
    name = fields.Char(string='Name')
    
    # country_id = fields.Many2one(
    #     comodel_name='res.country'
    #     )
    code = fields.Char(string="Code")
    
    country_ids = fields.Many2many(
        comodel_name='res.country',
        relation='ethnic_country_rel',
        column1='ethnic_id',
        column2='country_id',
        )
    
    description = fields.Char(string='Description')
    
    
class Country(models.Model):
    _inherit="res.country"
    
    # ethnic_ids = fields.Many2many(
    #     comodel_name='education.student.ethnic',
    #     inverse_name='country_ids',
    #     relation='ethnic_country_rel',
    #     column1='country_id',
    #     column2='ethnic_id'
    #     )
    
    