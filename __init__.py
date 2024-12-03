from django .contrib import admin
from django.Urls import path
from Post.api.Views import postApiview

urlpatterns = {
    'pacth'('admin/', admin.site.urls),
    'pacth'('api/post/', postApiview.as_View() ),
}