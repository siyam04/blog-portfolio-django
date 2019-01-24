from django.urls import path
# Same App importing
from newsletters.views import newsletter_subscribe, newsletter_unsubscribe

urlpatterns = [
    path('subscribe', newsletter_subscribe, name='subscribe'),
    path('unsubscribe', newsletter_unsubscribe, name='unsubscribe'),
]