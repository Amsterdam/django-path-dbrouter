from .middleware import request_info


class DatabaseRouter:
    def _default_db(self):
        from django.conf import settings

        if (
            hasattr(request_info, "dataset")
            and request_info.dataset in settings.DATABASES
        ):
            return request_info.dataset
        else:
            return "default"

    def db_for_read(self, model, **hints):
        return self._default_db()

    def db_for_write(self, model, **hints):
        return self._default_db()

