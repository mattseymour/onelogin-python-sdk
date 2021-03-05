#!/usr/bin/python

from onelogin.api.util.utils import str2int, str2date

from .base import Base
from .group import Group
from .role import Role


class Event(Base):
    def __init__(self, data):
        self.id = str2int(data.get('id', None))
        self.created_at = str2date(data.get('created_at', None))
        self.account_id = str2int(data.get('account_id', None))
        self.user_id = str2int(data.get('user_id', None))
        self.user_name = data.get('user_name', '')
        self.event_type_id = str2int(data.get('event_type_id', None))
        self.notes = data.get('notes', '')
        self.ipaddr = data.get('ipaddr', '')
        self.actor_user_id = str2int(data.get('actor_user_id', None))
        self.actor_user_name = data.get('actor_user_name', '')
        self.assuming_acting_user_id = str2int(data.get('assuming_acting_user_id', None))
        self.role_id = str2int(data.get('role_id', None))
        self.role_name = data.get('role_name', '')
        self.app_id = str2int(data.get('app_id', None))
        self.app_name = data.get('app_name', None)
        self.group_id = str2int(data.get('group_id', None))
        self.group_name = data.get('group_name', '')
        self.otp_device_id = str2int(data.get('otp_device_id', None))
        self.otp_device_name = data.get('otp_device_name', '')
        self.policy_id = str2int(data.get('policy_id', None))
        self.policy_name = data.get('policy_name', '')
        self.actor_system = data.get('actor_system', '')
        self.custom_message = data.get('custom_message', '')
        self.operation_name = data.get('operation_name', '')
        self.directory_sync_run_id = str2int(data.get('directory_sync_run_id', None))
        self.directory_id = str2int(data.get('directory_id', None))
        self.resolution = data.get('resolution', '')
        self.client_id = data.get('client_id', None)
        self.resource_type_id = str2int(data.get('resource_type_id', None))
        self.error_description = data.get('error_description', '')
        self.proxy_ip = data.get('proxy_ip', None)
        self.risk_score = data.get('risk_score', None)
        self.risk_reasons = data.get('risk_reasons', None)
        self.risk_cookie_id = data.get('risk_cookie_id', None)
        self.browser_fingerprint = data.get('browser_fingerprint', None)

    def get_role(self):
        role = None
        if self.role_id is not None and self.role_name:
            role = Role(self.role_id, self.role_name)
        return role

    def get_group(self):
        group = None
        if self.group_id is not None and self.group_name:
            group = Group(self.group_id, self.group_name)
        return group
