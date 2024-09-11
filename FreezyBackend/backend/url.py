from django.urls import path
from .views import homepage,api_data


urlpatterns = [
    path('', homepage, name="homepage"),
    path('api/data/', api_data, name='api_data'),
    
    
]