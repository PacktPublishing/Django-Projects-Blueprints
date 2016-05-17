from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from frontend.views import CarDetailsView
from frontend.views import NewBookingView
from frontend.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^car/(?P<pk>\d+)/$', CarDetailsView.as_view(), name='car-details'),

    url(r'^booking/(?P<car_pk>\d+)/$', NewBookingView.as_view(), name='new-booking'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
