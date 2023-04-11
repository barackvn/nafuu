from odoo import models,api

class product_attribute_value(models.Model):
    _inherit = "product.attribute.value"
    
    @api.multi
    def get_attribute_values(self,name,attribute_id,auto_create=False):
        if attribute_values := self.search(
            [('name', '=ilike', name), ('attribute_id', '=', attribute_id)]
        ):
            return attribute_values
        else:
            return (
                self.create(({'name': name, 'attribute_id': attribute_id}))
                if auto_create
                else False
            )