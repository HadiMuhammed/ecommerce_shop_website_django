from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path("",views.index,name="home"),
    path("register/",views.register_user,name='register'),
    path("login/",views.login_user,name='login'),
    path("logout/",views.logout_user,name='logout'),
    path("add_to_cart/",views.add_to_cart,name="add_to_cart"),
    path("mycart/",views.mycart,name="mycart"),
    path("delete_from_cart/",views.delete_from_cart,name="delete_from_cart")
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)