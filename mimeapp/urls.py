from django.urls import path
from .views import Htmlview,xmlView,ExcelView
urlpatterns=[
    path('html',Htmlview.as_view()),
    path('xml',xmlView.as_view()),
    path('excel',ExcelView.as_view())
]
