from odoo import models, fields

class AcademyEnrollmentWizard(models.TransientModel):
    _name='academy.enrollment.wizard'
    _description='Academy Enrollment'    
    
    student_ids = fields.Many2many(
        comodel_name='education.student',
        string='Students'
        )
    
    class_ids = fields.Many2many(
        comodel_name='education.class',
        string='Class Name'
        )
    
    register_date = fields.Datetime('Enrollment Time')
    
    def action_enroll_class_apply(self):
        active_model = self.env.context.get('active_model') #Mục đích: Để xác định xem mình đang ở model nào trong ngữ cảnh đang thực hiện.
        class_id = self.env[active_model].browse(self.env.context.get('active_ids'))
        student_id = self.student_ids
        #
        vals_list = []
        for st in student_id:
            for cls in class_id:
                vals = {
                    'class_id': cls.id,
                    'student_id': st.id,
                    'register_date': self.register_date,
                }
                vals_list.append(vals)
        self.env['academy.enrollment'].create(vals_list)
        # return class_id.action_enroll_class_apply(enrollment=self.student_ids.id)
        return    
      