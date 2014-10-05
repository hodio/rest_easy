from permission.logics import AuthorPermissionLogic, CollaboratorsPermissionLogic, GroupInPermissionLogic

'''
EXAMPLE
PERMISSION_LOGICS = (
    ('your_app.Article', AuthorPermissionLogic()),
    ('your_app.Article', CollaboratorsPermissionLogic()),
)
'''

PERMISSION_LOGICS = (
    ('example.Person', AuthorPermissionLogic(field_name='user',)),
    ('example.Person', CollaboratorsPermissionLogic()),
)