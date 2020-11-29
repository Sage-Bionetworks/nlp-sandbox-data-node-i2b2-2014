# coding: utf-8

from __future__ import absolute_import
import pytest
import unittest

from flask import json
from mongoengine import connect, disconnect
from six import BytesIO

from openapi_server.dbmodels.dataset import Dataset as DbDataset
from openapi_server.models.dataset import Dataset  # noqa: E501
from openapi_server.models.error import Error  # noqa: E501
from openapi_server.models.page_of_datasets import PageOfDatasets  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDatasetController(BaseTestCase):
    """DatasetController integration test stubs"""

    def setUp(self):
        connect('mongoenginetest', host='mongomock://localhost')
        DbDataset.objects().delete()

    def tearDown(self):
        disconnect(alias='mongoenginetest')

    def _create_dataset(self, dataset_id):
        DbDataset(name='datasets/{dataset_id}'.format(
            dataset_id=dataset_id)
        ).save()

    def test_create_dataset(self):
        """Test case for create_dataset

        Create a dataset
        """
        dataset = {}
        query_string = [('datasetId', 'awesome-dataset')]
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets',
            method='POST',
            headers=headers,
            data=json.dumps(dataset),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_dataset(self):
        """Test case for delete_dataset

        Delete a dataset by ID
        """
        self._create_dataset("awesome-dataset")

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}'.format(
                dataset_id='awesome-dataset'
            ),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_dataset(self):
        """Test case for get_dataset

        Get a dataset by ID
        """
        self._create_dataset("awesome-dataset")

        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets/{dataset_id}'.format(
                dataset_id='awesome-dataset'
            ),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_datasets(self):
        """Test case for list_datasets

        Get all datasets
        """
        self._create_dataset("awesome-dataset")

        query_string = [('limit', 10),
                        ('offset', 0)]
        headers = {
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/api/v1/datasets',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()