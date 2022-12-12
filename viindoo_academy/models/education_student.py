from odoo import models, fields, api #models: Nơi chứa tất cả các quan hệ giữa các đối tương. models được sử dụng rất nhiều khi lập trình, hầu hết
    
"""
Đọc thêm về Mối quan hệ các trường trong cơ sở dữ liệu

- Cơ sở dữ liệu quan hệ
- Quan hệ cơ sở dữ liệu
- Primary key
- Freign Key

"""

class EducationStudent(models.Model):
    _name="education.student"
    _description="Education Student"
    
    name= fields.Char(
        string="Name",
        required=True,
        )
    
    class_id= fields.Many2one(
        comodel_name='education.class', # Tham số bắt buộc: Tên đối tượng đối ứng trong mối quan hệ.
        string='Class',
        )
    
    class_ids= fields.Many2many(
        comodel_name='education.class',
        relation='class_education_ref',
        column1='student_id',
        column2='class_id',
        string='Enrolled Classes'
        )
    
    year = fields.Char(
        string = 'Year of Birth'
        )
    
    age = fields.Integer(
        string = 'Age'
        )    

    ethnic_id = fields.Many2one(
        comodel_name = 'education.student.ethnic',
        string = 'Ethnic'
        ) 
    ethnic_code = fields.Char(related='ethnic_id.code', store=True)
    
    country_id = fields.Many2one(
        comodel_name = 'res.country',
        string = 'Country'
        )
       
    user_id = fields.Many2one(comodel_name = 'res.users', string = 'User') 
    
    @api.onchange('ethnic_id')
    def _onchange_ethnic_id(self):
        if self.ethnic_id:
            self.country_id = self.ethnic_id.country_ids[:1]

    