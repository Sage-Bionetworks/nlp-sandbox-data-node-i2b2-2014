# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server.models.dataset import Dataset
from openapi_server.models.page_of_datasets_all_of import PageOfDatasetsAllOf
from openapi_server.models.response_page_metadata import ResponsePageMetadata
from openapi_server.models.response_page_metadata_links import ResponsePageMetadataLinks
from openapi_server import util

from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.page_of_datasets_all_of import PageOfDatasetsAllOf  # noqa: E501
from openapi_server.models.response_page_metadata import ResponsePageMetadata  # noqa: E501
from openapi_server.models.response_page_metadata_links import ResponsePageMetadataLinks  # noqa: E501

class PageOfDatasets(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, offset=None, limit=None, links=None, datasets=None):  # noqa: E501
        """PageOfDatasets - a model defined in OpenAPI

        :param offset: The offset of this PageOfDatasets.  # noqa: E501
        :type offset: int
        :param limit: The limit of this PageOfDatasets.  # noqa: E501
        :type limit: int
        :param links: The links of this PageOfDatasets.  # noqa: E501
        :type links: ResponsePageMetadataLinks
        :param datasets: The datasets of this PageOfDatasets.  # noqa: E501
        :type datasets: List[Dataset]
        """
        self.openapi_types = {
            'offset': int,
            'limit': int,
            'links': ResponsePageMetadataLinks,
            'datasets': List[Dataset]
        }

        self.attribute_map = {
            'offset': 'offset',
            'limit': 'limit',
            'links': 'links',
            'datasets': 'datasets'
        }

        self._offset = offset
        self._limit = limit
        self._links = links
        self._datasets = datasets

    @classmethod
    def from_dict(cls, dikt) -> 'PageOfDatasets':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PageOfDatasets of this PageOfDatasets.  # noqa: E501
        :rtype: PageOfDatasets
        """
        return util.deserialize_model(dikt, cls)

    @property
    def offset(self):
        """Gets the offset of this PageOfDatasets.

        Index of the first result that must be returned  # noqa: E501

        :return: The offset of this PageOfDatasets.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOfDatasets.

        Index of the first result that must be returned  # noqa: E501

        :param offset: The offset of this PageOfDatasets.
        :type offset: int
        """
        if offset is None:
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOfDatasets.

        Maximum number of results returned  # noqa: E501

        :return: The limit of this PageOfDatasets.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOfDatasets.

        Maximum number of results returned  # noqa: E501

        :param limit: The limit of this PageOfDatasets.
        :type limit: int
        """
        if limit is None:
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def links(self):
        """Gets the links of this PageOfDatasets.


        :return: The links of this PageOfDatasets.
        :rtype: ResponsePageMetadataLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PageOfDatasets.


        :param links: The links of this PageOfDatasets.
        :type links: ResponsePageMetadataLinks
        """
        if links is None:
            raise ValueError("Invalid value for `links`, must not be `None`")  # noqa: E501

        self._links = links

    @property
    def datasets(self):
        """Gets the datasets of this PageOfDatasets.

        An array of datasets  # noqa: E501

        :return: The datasets of this PageOfDatasets.
        :rtype: List[Dataset]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this PageOfDatasets.

        An array of datasets  # noqa: E501

        :param datasets: The datasets of this PageOfDatasets.
        :type datasets: List[Dataset]
        """

        self._datasets = datasets
