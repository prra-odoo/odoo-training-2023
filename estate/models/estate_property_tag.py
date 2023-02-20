from odoo import models, fields, api


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tags"

    _sql_constraints = [("tag_uniq", "UNIQUE (name)",
                         "The tag must be different from already defined tag names."),
                        ("type_notnull", "CHECK (name IS NOT NULL)",
                         "Property tag cannot be empty."),]

    name = fields.Char(string='Tag Name')
    cap_name = fields.Char(compute='capital_name', store=True)

    @api.depends("name")
    def capital_name(self):
        # print("---------------------------------------------------")
        for record in self:
            if (record.name):
                # print("--------------------------------------------------------")
                record.cap_name = record.name.upper()
            else:
                record.cap_name = ''
        return True
        # pass
