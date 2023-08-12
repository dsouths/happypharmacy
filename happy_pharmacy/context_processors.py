from django.conf import settings


def media(request):
    """
    Add media-related context variables to the context.
    """
    return {'MEDIA_URL': settings.MEDIA_URL}