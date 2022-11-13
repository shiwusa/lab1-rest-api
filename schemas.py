from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_name = fields.Str(required=True)
    category_title = fields.Str(required=True)
    title = fields.Str(required=True)
    amount = fields.Float(required=True)
    date = fields.Str(dump_only=True)



