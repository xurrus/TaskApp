from odoo import models, fields


class category_app(models.Model):
    _name = 'task_app.category_model'
    _description = 'Category Model'

    name = fields.Char(string="Category Name",help="The name of the category",required=True,index=True)
    description = fields.Html(string="Description",help="Description of the category",required=True)
    tasks = fields.One2many(comodel_name="task_app.task_model", inverse_name="category",string="Tasks")