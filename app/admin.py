# -*- coding: UTF-8 -*-
from rest_framework.authtoken.admin import TokenAdmin
TokenAdmin.raw_id_fields = ['user']