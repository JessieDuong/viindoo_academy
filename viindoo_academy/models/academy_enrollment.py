from odoo import models, fields

class AcademyEnrollment(models.Model):
    _name='academy.enrollment'
    _description='Academy Enrollment'
    
    name = fields.Char(
        string='Register Code')
    
    student_id = fields.Many2one(
        comodel_name='education.student',
        string='Students'
        )
    
    class_id = fields.Many2one(
        comodel_name='education.class',
        string='Registered Class',
        )
    
    register_date = fields.Date(
        string='Enrollment Time')

