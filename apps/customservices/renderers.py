from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class JSONResponseRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = []
        if isinstance(data, dict) and (error := data.get('errors')):
            errors.extend(error)
            del data['errors']
        response_dict = {
            'result': data if data else {},
            'error': errors,
        }
        return json.dumps(response_dict)