from .base import *


# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'root': {
#         'level': 'DEBUG',
#         # Adding the watchtower handler here causes all loggers in the project that
#         # have propagate=True (the default) to send messages to watchtower. If you
#         # wish to send only from specific loggers instead, remove "watchtower" here
#         # and configure individual loggers below.
#         # 'handlers': ['watchtower', 'console'],
#         'handlers': ['console'],
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#         # 'watchtower': {
#         #     'class': 'watchtower.CloudWatchLogHandler',
#         #     'boto3_client': boto3_logs_client,
#         #     'log_group_name': 'inventoryManagementApp',
#         #     # Decrease the verbosity level here to send only those logs to watchtower,
#         #     # but still see more verbose logs in the console. See the watchtower
#         #     # documentation for other parameters that can be set here.
#         #     'level': 'DEBUG'
#         # }
#     },
#     'loggers': {
#         # In the debug server (`manage.py runserver`), several Django system loggers cause
#         # deadlocks when using threading in the logging handler, and are not supported by
#         # watchtower. This limitation does not apply when running on production WSGI servers
#         # (gunicorn, uwsgi, etc.), so we recommend that you set `propagate=True` below in your
#         # production-specific Django settings file to receive Django system logs in CloudWatch.
#         'django': {
#             'level': 'DEBUG',
#             'handlers': ['console'],
#             'propagate': False
#         }
#         # Add any other logger-specific configuration here.
#     }
# }
