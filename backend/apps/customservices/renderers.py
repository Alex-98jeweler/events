from rest_framework.renderers import JSONRenderer
from rest_framework.utils import json


class JSONResponseRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        if "response" in renderer_context:
            response = renderer_context['response']
            if 400 <= response.status_code < 500:
                response_dict = {
                    "errors" : data,
                    "result": []
                }
            elif 200 <= response.status_code < 300:
                response_dict = {
                    "errors": None,
                    "result": data,
                }
        return json.dumps(response_dict)