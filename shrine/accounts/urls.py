from django.conf.urls import url
from accounts import views


urlpatterns = [
     url(r"^registration/$", views.Registration.as_view(), name="registration"),
 ]
