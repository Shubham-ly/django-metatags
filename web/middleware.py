from django.http import HttpRequest, HttpResponse
from django.urls import resolve
from .data import data as metadata


class SEOMetaTagsMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
    
    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_template_response(self, request: HttpRequest, response: HttpResponse):
        page = resolve(request.path_info).url_name 

        # TODO: Query metadata [name, description, ...] of the requested page and add to response_context
        response.context_data["metadata"] = metadata[page]

        return response


