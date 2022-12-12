from odoo import models, fields

class EducationTechnical(models.Model):
    _name = 'education.technical'
    _description = 'Education Technical'
    
    
    name = fields.Char(
        string = "Technical Class Name",      
        required = True,
        help = "The name of Technical Class",
        )
    
    state = fields.Selection(
        [
         ('draft', 'Draft'),
         ('confirm', 'Confirm'),
         ('done','Done'),
         ('cancel', 'Cancel'),  
            ],
        string = "Status",
        default = 'draft',
        help = 'Status of Class'
        )
    description = fields.Char(
        string = "Descriptions",
        )
    
    year = fields.Integer(
        string = "Year of birth",
        )
    
    age = fields.Integer(
        string = "Your age",
        )
    active = fields.Boolean(default=True)
    