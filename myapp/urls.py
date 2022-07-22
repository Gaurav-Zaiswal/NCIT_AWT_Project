from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from socialApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(
        template_name="socialapp/login.html"
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name = "socialapp/login.html",
        next_page = reverse_lazy('login')
    ), name='logout'),
    path('', include('socialApp.urls')),
]



admin.site.site_header = 'Powered by Advanced CMS'
admin.site.site_title  = 'advancedcms'
# admin.site.index_title   = '' # to update "Site Adminstrator" text on Admin's Dashboard
 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)