from django.urls import path

from .views import HomepageView,AboutPageView, SignUpView

urlpatterns = [
    path('', HomepageView.as_view(), name ='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('signup/', SignUpView.as_view(), name='signup'), 

]