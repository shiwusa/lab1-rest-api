from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    private = fields.Bool(required=False, default=False)
    owner_id = fields.Int(required=False)


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    title = fields.Str(required=True)
    amount = fields.Float(required=True)
    date = fields.Str(dump_only=True)



