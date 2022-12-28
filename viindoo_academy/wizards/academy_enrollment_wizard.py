from odoo import models, fields, api, _
from odoo.exceptions import UserError

class WizardEnrollmentSingle(models.TransientModel):
    _name='wizard.enrollment.single'
    _description='Single Enrollment Wizard'  
    
    registration_number = fields.Char()
    class_id = fields.Many2one('education.class', string='Class',required=True )
    student_id = fields.Many2one('education.student', string='Student',required=True)
    date = fields.Date(default=fields.Date.today,
                       help="The date on which the student enrolls")
    active_model = fields.Char()
    wizard_multi_id = fields.Many2one(comodel_name='wizard.enrollment.multi')
    # Hàm lấy dữ liệu mặc định.
    @api.model
    def default_get(self, fields_list):
        res = super().default_get(fields_list)
        
        active_model = self._context.get('active_model')
        active_id = self._context.get('active_id')
        
        if active_model == 'education.class':
            res['class_id'] = active_id    
        elif active_model == 'education.student':
            res['student_id'] = active_id    
        res['active_model'] = active_model
        res['date'] = fields.Date.today()
        return res
    
    def enroll(self):
        # Nếu khi khai báo trường class_id và student_id mà đã có thuộc tính required=True thì không cần đoạn code check Error này nữa.
        if not self.class_id or not self.student_id:
            raise UserError(_("You must specify both class and student first."))
        
        self.env['academy.enrollment'].create({
            'name': self.registration_number,
            'class_id': self.class_id.id,
            'student_id': self.student_id.id,
            'date': self.date or fields.Date.today()})
#
# class AcademyEnrollmentWizard(models.TransientModel):
#     _name='academy.enrollment.wizard'
#     _description='Academy Enrollment'    
#
#     student_ids = fields.Many2many(
#         comodel_name='education.student',
#         string='Students'
#         )
#
#     class_ids = fields.Many2many(
#         comodel_name='education.class',
#         string='Class Name'
#         )
#
#     register_date = fields.Datetime('Enrollment Time')
#
#     def action_enroll_class_apply(self):
#         active_model = self.env.context.get('active_model') #Mục đích: Để xác định xem mình đang ở model nào trong ngữ cảnh đang thực hiện.
#         class_id = self.env[active_model].browse(self.env.context.get('active_ids'))
#         student_id = self.student_ids
#         #
#         vals_list = []
#         for st in student_id:
#             for cls in class_id:
#                 vals = {
#                     'class_id': cls.id,
#                     'student_id': st.id,
#                     'register_date': self.register_date,
#                 }
#                 vals_list.append(vals)
#         self.env['academy.enrollment'].create(vals_list)
#         # return class_id.action_enroll_class_apply(enrollment=self.student_ids.id)
#         return    
#

class WizardEnrollmentMulti(models.TransientModel):
    _name='wizard.enrollment.multi'
    _description='Multi Enrollment Wizard'  
    
    line_ids = fields.One2many(comodel_name='wizard.enrollment.single', inverse_name='wizard_multi_id')
      
    def enrollmulti(self):
        vals_list = []
        active_model = self._context.get('active_model') #_context là từ self
        records = self.env[active_model].browse(self.env.context.get('active_ids'))  #context là phương thức của env nên việc lấy self._context sẽ giống như env.context
        for record in records:
            for line in self.line_ids:
                vals_list.append({
                    'name': line.registration_number,
                    'class_id': record.id if active_model == 'education.class' else line.class_id.id,
                    'student_id': record.id if active_model == 'education.student' else line.student_id.id,
                    'date': line.date or fields.Date.today()                    
                    })
        self.env['academy.enrollment'].create(vals_list)

    
