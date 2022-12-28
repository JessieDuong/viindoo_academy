from odoo import models, fields, api#models: Nơi chứa tất cả các quan hệ giữa các đối tương. models được sử dụng rất nhiều khi lập trình, hầu hết
from odoo.exceptions import ValidationError

                                #fields: Là một module trong python, nơi chứa các class định nghĩa ra các trường với kiểu dữ liệu khác nhau

class EducationClass(models.Model):
    _name = 'education.class'
    _description = 'Education Class'

    name = fields.Char(
        string = 'Name', # quy định tên trường
        help = "The name of the class for identify",
        required=True, # 
        index=False, #yêu cầu cơ sở dữ liệu lập chỉ mục cho trường này để khi tìm kiếm được nhanh hơn
        )
    # Khai báo các trạng thái của bản ghi.
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('done', 'Done'),
            ('cancel', 'Cancel'),
            ],
        required=True, #vừa để required người dùng cần nhập giá atrị cho trường này, vừa để không có state = null
        string='Status',
        default='draft',
        help='Status of class',
        )
    
    description = fields.Char(
        string = 'Description',
        )
    
    year = fields.Char(
        string = 'Year'
        )
    
    start_date = fields.Datetime(string = "Start Date")
    end_date = fields.Datetime(string = "End Date")    
    
    #Khai báo trường lưu trữ/ không lưu trữ (archived/unarchived) một số bản ghi
    active = fields.Boolean(default=True) 
    #active = fields.Boolean(default=True) để default=True thì mặc định sẽ là KHÔNG Lưu trữ hoặc KHÔNG tích. Mặc định default = False.

    student_ids= fields.One2many(
        comodel_name='education.student',
        inverse_name='class_id',
        string='Student',
        help='The student that belong to the class'
        )
    
    historical_student_ids= fields.Many2many(
        comodel_name='education.student',
        relation='class_education_ref',
        column1='class_id',
        column2='student_id',
        string='Historical Students'
        )
    students_count = fields.Integer(
        string = 'Students Count',
        store = True,
        compute = '_compute_student',
        )
    
    historical_students_count = fields.Float(
        string = 'Historical Student Count',
        store = True,
        compute = '_compute_historical_students',
        )

    company_id = fields.Many2one(  #Nhiều class cho một công ty)
        comodel_name='res.company',
        string = 'Company',
        default = lambda self: self.env.company,
        )
    
    responsible_id = fields.Many2one(comodel_name='res.users', string='Responsible user', default = lambda self: self.env.user)
    
    _sql_constraints = [
        ('unique_class_name','unique(name)','The class name must be unique'),
        ]    
    # @api.onchange('name')
    # def _onchange_name(self):
    #     if self.name:
    #         self.students_count = self.
    
    @api.depends('student_ids')
    def _compute_student(self):
        for r in self:
            r.students_count = len(r.student_ids)
    
    @api.depends('historical_student_ids')
    def _compute_historical_students(self):
        for r in self:
            r.historical_students_count = len(r.historical_student_ids)
    
    @api.constrains('start_date','end_date')
    def _check_date(self):
        for r in self:
            if r.start_date and r.end_date and r.start_date > r.end_date:
                raise ValidationError("Start date must be earlier than End date")

# Tìm tất cả các bản ghi country trong model res.country thỏa mãn điều kiện search name = abc và language = tiếng việt
#     def test(self): 
#         countries = self.env['res.country'].search([
#             ('name','=','abc'),
#             ('language','=','Tieng Viet')
#             ])
#
# # Tìm các country có tên là abc và ngôn ngữ là tiếng việt hoặc tiếng trung.          
#         countries1 = self.env['res.country'].search([
#             '&',
#             ('name','=','abc'),
#             '|',
#             ('language','=','Tieng Viet')
#             ('language','=','Tieng Trung')
#             ])
# """        
# '=?'  
# '=like': Chỉ dùng cho string, bằng đúng số lượng ký tự và đúng chữ hoa, chữ thường
# '=ilike': 
# 'like'
# 'not like'
# 'ilike'
# 'not ilike'
# 'child-of'
#
# """    
    
    