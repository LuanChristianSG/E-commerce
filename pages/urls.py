from django.urls import path

from .views import SupportPageView, HomePageView

app_name = 'pages'

urlpatterns = [
    path('support/', SupportPageView.as_view(), name='support'),
    path('', HomePageView.as_view(), name='home'),

]