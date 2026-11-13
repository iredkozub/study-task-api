import unittest

from flask import json

from openapi_server.models.api_error import ApiError  # noqa: E501
from openapi_server.models.task_create import TaskCreate  # noqa: E501
from openapi_server.models.task_response import TaskResponse  # noqa: E501
from openapi_server.models.task_update import TaskUpdate  # noqa: E501
from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_create_task(self):
        """Test case for create_task

        Создать учебную задачу
        """
        task_create = {"title":"title","subject":"subject","dueDate":"2000-01-23"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/tasks',
            method='POST',
            headers=headers,
            data=json.dumps(task_create),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_task(self):
        """Test case for delete_task

        Удалить учебную задачу
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/tasks/{id}'.format(id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_task_by_id(self):
        """Test case for get_task_by_id

        Получить учебную задачу по ID
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/tasks/{id}'.format(id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_tasks(self):
        """Test case for get_tasks

        Получить список учебных задач
        """
        query_string = [('status', 'status_example')]
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/tasks',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_task(self):
        """Test case for update_task

        Обновить учебную задачу
        """
        task_update = {"title":"title","subject":"subject","dueDate":"2000-01-23","status":"pending"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/tasks/{id}'.format(id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(task_update),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
