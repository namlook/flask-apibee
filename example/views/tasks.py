
from flask import Blueprint
from flaskext.api import api, NotFound

tasks = Blueprint('tasks', __name__, url_prefix='/tasks')

class Task(dict):
    """
    This object does nothing. It's purpose if only for example. It's usuly a db model
    """
    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        if kwargs.get('id'):
            id = kwargs['id']
            self.update({'title': 'task %s' % id, 'text': 'bla'*int(id)})

@tasks.route('/info')
def info():
    return "coucou"

@tasks.route('/new')
@api(required=['title'], optional={'text':None})
def new_task(**args):
    task = Task()
    task['title'] = args['title']
    task['text'] = args['text']
    return task

@tasks.route('/get')
@api(required=['id'])
def get(**args):
    task_id = args['id']
    try:
        return Task(id=task_id)
    except:
        raise NotFound("task not found")

@tasks.route('/list')
@api(optional={'limit':10})
def list_task(**args):
    limit = args['limit']
    print range(limit)
    return [Task(id=task_id) for task_id in range(limit)]

