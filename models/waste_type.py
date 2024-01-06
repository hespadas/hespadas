from odoo import models, fields


class WasteType(models.Model):
    _name = "waste.type"
    _description = "Waste Type"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    collection_point_ids = fields.Many2many(
        "collection.point",
        string="Collection Points",
        help="Collection points that collect this type of waste.",
    )
