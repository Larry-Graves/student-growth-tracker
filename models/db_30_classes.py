# -*- coding: utf-8 -*-

db.define_table(
    'classes',
    Field('name', required=True, requires=IS_NOT_EMPTY()),
    Field('grade_level', 'integer', required=True, requires=IS_NOT_EMPTY()),
    Field('start_date', 'datetime', required=True, requires=IS_NOT_EMPTY()),
    Field('end_date', 'datetime', required=True, requires=IS_NOT_EMPTY()),
    Field('content_area', 'reference contentarea'),
    format = '%(name)s')

db.classes.id.readable = db.classes.id.writable = False

if __name__ == '__main__':
    pass
