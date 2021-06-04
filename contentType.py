from django.contrib.contenttypes.models import ContentType

from core.exceptions import AppException


class ModelWrapper:
    """Model Helper Mixin"""

    @classmethod
    def get_content_type(cls, app_label: str, model: str) -> ContentType:
        """Get content type

        :param app_label: app_label
        :param model: model name
        :return: ContentType Object
        """
        try:
            ct = ContentType.objects.get(app_label=app_label, model=model)
        except ContentType.DoesNotExist:
            raise AppException(f"Invalid Content Type ({app_label}:{model})")
        return ct

    @classmethod
    def get_model(cls, app_label: str, model: str):
        """Get model class

        :param app_label: app name
        :param model: model name
        :return: model class
        """
        ct = cls.get_content_type(app_label, model)
        return ct.model_class()

    @classmethod
    def get_instance(cls, app_label: str, model: str, object_id: int):
        """Get object instance using content type

        :param app_label: app name
        :param model: model name
        :param object_id: object id
        :return: object
        """
        model_cls = cls.get_model(app_label, model)
        try:
            instance = model_cls.objects.get(id=object_id)
        except model_cls.DoesNotExist:
            raise AppException(f"{model} Object with id {object_id} does not exists")
        return instance
