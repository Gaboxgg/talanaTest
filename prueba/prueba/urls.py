from django.contrib import admin
from django.conf.urls import url
from APP.views import login , logout , buscar_autos

urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^ajax/buscar_autos/$', buscar_autos, name='buscar_autos'),
	url(r'', login),
]