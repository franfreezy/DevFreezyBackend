from django.urls import path
from .views import homepage,api_data,stk_push_callback,index


urlpatterns = [
    path('', homepage, name="homepage"),
    path('api/data/', api_data, name='api_data'),
    path('index/', index, name='index'),
    path('daraja/stk-push', stk_push_callback, name='mpesa_stk_push_callback')
    
    
]