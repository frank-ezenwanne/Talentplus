from django.urls import path
from .api import GetCompanyName,PostCompanyName,ListUrlsView

urlpatterns = [
    path('api/create_company',PostCompanyName.as_view()),
    path('api/get_company_name',GetCompanyName.as_view()),
    path('api',ListUrlsView.as_view())
]