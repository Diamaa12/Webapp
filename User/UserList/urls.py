
from contacts.views import index, add_contact, del_user

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("add/", add_contact, name="add-contact"),
    path("delete/", del_user, name="del-user")
]
