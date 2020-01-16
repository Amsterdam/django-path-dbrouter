import logging
import threading
from django.conf import settings
from django.http import Http404

request_info = threading.local()

logger = logging.getLogger("django")


class RouterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        try:
            path = request.path.split(settings.URI_PATH_PREFIX)[1]
            dataset = path.split("/")[0]
            if dataset not in settings.DATABASES:
                raise IndexError
        except IndexError:
            raise Http404(f"dataset {dataset} does not exist")
        request_info.dataset = dataset
        logger.info(dataset)
        response = self.get_response(request)
        del request_info.dataset

        return response
