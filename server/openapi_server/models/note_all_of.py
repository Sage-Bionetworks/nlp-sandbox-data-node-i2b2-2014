# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
import re
from openapi_server import util

import re  # noqa: E501

class NoteAllOf(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, type=None):  # noqa: E501
        """NoteAllOf - a model defined in OpenAPI

        :param name: The name of this NoteAllOf.  # noqa: E501
        :type name: str
        :param type: The type of this NoteAllOf.  # noqa: E501
        :type type: str
        """
        self.openapi_types = {
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type'
        }

        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'NoteAllOf':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Note_allOf of this NoteAllOf.  # noqa: E501
        :rtype: NoteAllOf
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this NoteAllOf.

        The name of the note  # noqa: E501

        :return: The name of this NoteAllOf.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NoteAllOf.

        The name of the note  # noqa: E501

        :param name: The name of this NoteAllOf.
        :type name: str
        """
        if name is not None and len(name) > 60:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `60`")  # noqa: E501
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")  # noqa: E501
        if name is not None and not re.search(r'^[a-z0-9]+(?:-[a-z0-9]+)*$', name):  # noqa: E501
            raise ValueError("Invalid value for `name`, must be a follow pattern or equal to `/^[a-z0-9]+(?:-[a-z0-9]+)*$/`")  # noqa: E501

        self._name = name

    @property
    def type(self):
        """Gets the type of this NoteAllOf.

        The note type (LOINC concept)  # noqa: E501

        :return: The type of this NoteAllOf.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NoteAllOf.

        The note type (LOINC concept)  # noqa: E501

        :param type: The type of this NoteAllOf.
        :type type: str
        """

        self._type = type