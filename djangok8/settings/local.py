import dj_database_url

from .common import *

# postgres://USER:PASSWORD@HOST:PORT/NAME
DATABASES = {
    'default': dj_database_url.config(
      default='postgres://postgres:postgres@172.20.0.3/postgres'
    ),
}
#
# LOGGING = {
#     'version': 1,
#     # 'disable_existing_loggers': False,
#
#     'handlers': {
#         'gelf': {
#             'class': 'graypy.GELFHandler',
#             'host': 'localhost',
#             'port': 12201,
#         },
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         # ...
#         'projectname': {
#             # mail_admins will only accept ERROR and higher
#             'handlers': ['gelf', 'console'],
#             'level': 'DEBUG',
#         },
#     },
# }