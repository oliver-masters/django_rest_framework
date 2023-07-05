import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    body = request.body

    data = {}

    if body:
        data = json.loads(body)

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    return JsonResponse(data)
