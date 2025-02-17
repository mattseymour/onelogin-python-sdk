"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.0
    Contact: support@onelogin.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from onelogin.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from onelogin.exceptions import ApiAttributeError


def lazy_import():
    from onelogin.model.schema_provisioning import SchemaProvisioning
    globals()['SchemaProvisioning'] = SchemaProvisioning


class Schema(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('auth_method',): {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '6': 6,
            '7': 7,
            '8': 8,
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (int,),  # noqa: E501
            'connector_id': (int,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'description': (str,),  # noqa: E501
            'notes': (str,),  # noqa: E501
            'policy_id': (int,),  # noqa: E501
            'brand_id': (int,),  # noqa: E501
            'icon_url': (str,),  # noqa: E501
            'visible': (bool,),  # noqa: E501
            'auth_method': (int,),  # noqa: E501
            'tab_id': (int,),  # noqa: E501
            'created_at': (str,),  # noqa: E501
            'updated_at': (str,),  # noqa: E501
            'role_ids': ([int],),  # noqa: E501
            'allow_assumed_signin': (bool,),  # noqa: E501
            'provisioning': (SchemaProvisioning,),  # noqa: E501
            'sso': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'configuration': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'parameters': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
            'enforcement_point': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'connector_id': 'connector_id',  # noqa: E501
        'name': 'name',  # noqa: E501
        'description': 'description',  # noqa: E501
        'notes': 'notes',  # noqa: E501
        'policy_id': 'policy_id',  # noqa: E501
        'brand_id': 'brand_id',  # noqa: E501
        'icon_url': 'icon_url',  # noqa: E501
        'visible': 'visible',  # noqa: E501
        'auth_method': 'auth_method',  # noqa: E501
        'tab_id': 'tab_id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'role_ids': 'role_ids',  # noqa: E501
        'allow_assumed_signin': 'allow_assumed_signin',  # noqa: E501
        'provisioning': 'provisioning',  # noqa: E501
        'sso': 'sso',  # noqa: E501
        'configuration': 'configuration',  # noqa: E501
        'parameters': 'parameters',  # noqa: E501
        'enforcement_point': 'enforcement_point',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Schema - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): Apps unique ID in OneLogin.. [optional]  # noqa: E501
            connector_id (int): ID of the apps underlying connector.. [optional]  # noqa: E501
            name (str): App name.. [optional]  # noqa: E501
            description (str): Freeform description of the app.. [optional]  # noqa: E501
            notes (str): Freeform notes about the app.. [optional]  # noqa: E501
            policy_id (int): The security policy assigned to the app.. [optional]  # noqa: E501
            brand_id (int): The custom login page branding to use for this app. Applies to app initiated logins via OIDC or SAML.. [optional]  # noqa: E501
            icon_url (str): A link to the apps icon url.. [optional]  # noqa: E501
            visible (bool): Indicates if the app is visible in the OneLogin portal.. [optional]  # noqa: E501
            auth_method (int): An ID indicating the type of app.. [optional]  # noqa: E501
            tab_id (int): ID of the OneLogin portal tab that the app is assigned to.. [optional]  # noqa: E501
            created_at (str): The date the app was created.. [optional]  # noqa: E501
            updated_at (str): The date the app was last updated.. [optional]  # noqa: E501
            role_ids ([int]): List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided.. [optional]  # noqa: E501
            allow_assumed_signin (bool): Indicates whether or not administrators can access the app as a user that they have assumed control over.. [optional]  # noqa: E501
            provisioning (SchemaProvisioning): [optional]  # noqa: E501
            sso ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            configuration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            parameters ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            enforcement_point ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Schema - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (int): Apps unique ID in OneLogin.. [optional]  # noqa: E501
            connector_id (int): ID of the apps underlying connector.. [optional]  # noqa: E501
            name (str): App name.. [optional]  # noqa: E501
            description (str): Freeform description of the app.. [optional]  # noqa: E501
            notes (str): Freeform notes about the app.. [optional]  # noqa: E501
            policy_id (int): The security policy assigned to the app.. [optional]  # noqa: E501
            brand_id (int): The custom login page branding to use for this app. Applies to app initiated logins via OIDC or SAML.. [optional]  # noqa: E501
            icon_url (str): A link to the apps icon url.. [optional]  # noqa: E501
            visible (bool): Indicates if the app is visible in the OneLogin portal.. [optional]  # noqa: E501
            auth_method (int): An ID indicating the type of app.. [optional]  # noqa: E501
            tab_id (int): ID of the OneLogin portal tab that the app is assigned to.. [optional]  # noqa: E501
            created_at (str): The date the app was created.. [optional]  # noqa: E501
            updated_at (str): The date the app was last updated.. [optional]  # noqa: E501
            role_ids ([int]): List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided.. [optional]  # noqa: E501
            allow_assumed_signin (bool): Indicates whether or not administrators can access the app as a user that they have assumed control over.. [optional]  # noqa: E501
            provisioning (SchemaProvisioning): [optional]  # noqa: E501
            sso ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            configuration ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            parameters ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
            enforcement_point ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
