from odoo import models, fields


class task_app(models.Model):
    _name = 'task_app.task_model'
    _description = 'Task Model'

    name = fields.Text(string="Task Name",help="The name of the task",required=True,index=True)
    isdone = fields.Boolean(string="Is done?",help="Is the task done?")
    active = fields.Boolean(string="Is active?",help="Is the task active?",default=True)
    category = fields.Many2one(comodel_name="task_app.category_model",string="Category")