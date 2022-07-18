from django.conf import settings
from django.conf.urls.static import static
from django.urls import URLPattern, path
from .views import contact_view, card_view

urlpatterns = [
    path('', contact_view),
    path('', card_view),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
