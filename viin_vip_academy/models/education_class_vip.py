from odoo import fields,models

class EducationClassVip(models.Model):
    _inherit="education.class"
    _name="education.class.vip"
    _description="Education Class Vip"
    
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency"
        )
    
    credit = fields.Monetary(
        string="Credit"
        )
    
    historical_student_ids= fields.Many2many(
        comodel_name='education.student',
        relation='class_education_vip_rel',
        column1='class_id',
        column2='student_id',
        string='Historical Students Vip'
        )
    
    student_ids= fields.One2many(
        comodel_name='education.student',
        inverse_name='class_vip_id',
        string='Student',
        help='The student that belong to the class'
        )
    
class EducationStudentVip(models.Model):
    _inherit="education.student"
    
    class_vip_id = fields.Many2one(
        comodel_name = "education.class.vip",
        string = "Class Vip",
        )
    
    class_ids= fields.Many2many(
        comodel_name='education.class.vip',
        relation='class_education_vip_rel',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes'
        )    



