# -*- coding: utf-8 -*-

""" Endpoints class

Copyright (c) 2021, OneLogin, Inc.
All rights reserved.

Endpoints class of the OneLogin's Python SDK.

"""

from onelogin.api.util.constants import Constants


class Endpoints(object):
    """

    AUX API URL endpoints for the OneLogin's Python SDK.

    """

    matrix = {
        Constants.GET_USERS_URL: { "user": [1, 2 ] },
        Constants.GET_USER_URL: { "user": [1, 2] },
        Constants.GET_APPS_FOR_USER_URL: { "user": [1, 2] },
        Constants.GET_ROLES_FOR_USER_URL: { "user": [1] },
        Constants.GET_CUSTOM_ATTRIBUTES_URL: { "user": [1] },
        Constants.CREATE_USER_URL: { "user": [1, 2] },
        Constants.UPDATE_USER_URL: { "user": [1, 2] },
        Constants.DELETE_USER_URL: { "user": [1, 2] },
        Constants.ADD_ROLE_TO_USER_URL: { "user": [1] },
        Constants.DELETE_ROLE_TO_USER_URL: { "user": [1] },
        Constants.SET_PW_CLEARTEXT: { "user": [1] },
        Constants.SET_PW_SALT: { "user": [1] },
        Constants.SET_STATE_TO_USER_URL: { "user": [1] },
        Constants.SET_CUSTOM_ATTRIBUTE_TO_USER_URL: { "user": [1] },
        Constants.LOG_USER_OUT_URL: { "user": [1] },
        Constants.LOCK_USER_URL: { "user": [1] },
        Constants.GENERATE_MFA_TOKEN_URL: { "user": [1] },
        Constants.GET_APPS_URL: { "app": [1, 2] },
        Constants.GET_ROLES_URL: { "role": [1, 2] },
        Constants.CREATE_ROLE_URL: { "role": [2] },
        Constants.GET_ROLE_URL: { "role": [1, 2] },
        Constants.UPDATE_ROLE_URL: { "role": [2] },
        Constants.GET_ROLE_APPS_URL: { "role": [2] },
        Constants.SET_ROLE_APPS_URL: { "role": [2] },
        Constants.GET_ROLE_USERS_URL: { "role": [2] },
        Constants.ADD_ROLE_USERS_URL: { "role": [2] },
        Constants.REMOVE_ROLE_USERS_URL: { "role": [2] },
        Constants.GET_ROLE_ADMINS_URL: { "role": [2] },
        Constants.ADD_ROLE_ADMINS_URL: { "role": [2] },
        Constants.REMOVE_ROLE_ADMINS_URL: { "role": [2] },
        Constants.DELETE_ROLE_URL: { "role": [2] },
        Constants.GET_EVENT_TYPES_URL: { "event": [1] },
        Constants.GET_EVENTS_URL: { "event": [1] },
        Constants.CREATE_EVENT_URL: { "event": [1] },
        Constants.GET_EVENT_URL: { "event": [1] },
        Constants.GET_GROUPS_URL: { "group": [1] },
        Constants.CREATE_GROUP_URL: { "group": [1] },
        Constants.GET_GROUP_URL: { "group": [1] },
        Constants.SESSION_LOGIN_TOKEN_URL: { "custom_login": [1] },
        Constants.GET_TOKEN_VERIFY_FACTOR: { "custom_login": [1] },
        Constants.GET_SAML_ASSERTION_URL: { "assertion": [1, 2] },
        Constants.GET_SAML_VERIFY_FACTOR: { "assertion": [1, 2] },
        Constants.GET_FACTORS_URL: { "mfa": [1] },
        Constants.ENROLL_FACTOR_URL: { "mfa": [1] },
        Constants.GET_ENROLLED_FACTORS_URL: { "mfa": [1] },
        Constants.ACTIVATE_FACTOR_URL: { "mfa": [1] },
        Constants.VERIFY_FACTOR_URL: { "mfa": [1] },
        Constants.DELETE_FACTOR_URL: { "mfa": [1] },
        Constants.GENERATE_INVITE_LINK_URL: { "invite": [1] },
        Constants.SEND_INVITE_LINK_URL: { "invite": [1] },
        Constants.LIST_PRIVILEGES_URL: { "privilege": [1] },
        Constants.CREATE_PRIVILEGE_URL: { "privilege": [1] },
        Constants.UPDATE_PRIVILEGE_URL: { "privilege": [1] },
        Constants.GET_PRIVILEGE_URL: { "privilege": [1] },
        Constants.DELETE_PRIVILEGE_URL: { "privilege": [1] },
        Constants.GET_ROLES_ASSIGNED_TO_PRIVILEGE_URL: { "privilege": [1] },
        Constants.ASSIGN_ROLES_TO_PRIVILEGE_URL: { "privilege": [1] },
        Constants.REMOVE_ROLE_FROM_PRIVILEGE_URL: { "privilege": [1] },
        Constants.GET_USERS_ASSIGNED_TO_PRIVILEGE_URL: { "privilege": [1] },
        Constants.ASSIGN_USERS_TO_PRIVILEGE_URL: { "privilege": [1] },
        Constants.REMOVE_USER_FROM_PRIVILEGE_URL: { "privilege": [1] }
    }