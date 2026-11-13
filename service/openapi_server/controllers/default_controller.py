import flask
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.api_error import ApiError  # noqa: E501
from openapi_server.models.task_create import TaskCreate  # noqa: E501
from openapi_server.models.task_response import TaskResponse  # noqa: E501
from openapi_server.models.task_update import TaskUpdate  # noqa: E501
from openapi_server import util


def create_task(body):  # noqa: E501
    """Создать учебную задачу

     # noqa: E501

    :param task_create: 
    :type task_create: dict | bytes

    :rtype: Union[TaskResponse, Tuple[TaskResponse, int], Tuple[TaskResponse, int, Dict[str, str]]
    """
    task_create = body
    if flask.request.is_json:
        task_create = TaskCreate.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_task(id):  # noqa: E501
    """Удалить учебную задачу

     # noqa: E501

    :param id: Идентификатор учебной задачи
    :type id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_task_by_id(id):  # noqa: E501
    """Получить учебную задачу по ID

     # noqa: E501

    :param id: Идентификатор учебной задачи
    :type id: int

    :rtype: Union[TaskResponse, Tuple[TaskResponse, int], Tuple[TaskResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_tasks(status=None):  # noqa: E501
    """Получить список учебных задач

     # noqa: E501

    :param status: Фильтрация задач по статусу
    :type status: str

    :rtype: Union[List[TaskResponse], Tuple[List[TaskResponse], int], Tuple[List[TaskResponse], int, Dict[str, str]]
    """
    return 'do some magic!'


def update_task(id, body):  # noqa: E501
    """Обновить учебную задачу

     # noqa: E501

    :param id: Идентификатор учебной задачи
    :type id: int
    :param task_update: 
    :type task_update: dict | bytes

    :rtype: Union[TaskResponse, Tuple[TaskResponse, int], Tuple[TaskResponse, int, Dict[str, str]]
    """
    task_update = body
    if flask.request.is_json:
        task_update = TaskUpdate.from_dict(flask.request.get_json())  # noqa: E501
    return 'do some magic!'
