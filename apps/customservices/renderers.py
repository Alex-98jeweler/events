from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class JSONResponseRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        errors = {}
        print(data)
        if 'detail' in data:
            errors['detail'] = data['detail']
            del data['detail']
        if 'code' in data:
            errors['code'] = data['code']
            del data['code']
        if isinstance(data, dict) and (error := data.get('errors')):
            errors['errors_detailed'] = error
            del data['errors']
        response_dict = {
            'result': data if data else {},
            'error': errors,
        }
        return json.dumps(response_dict)