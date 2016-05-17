from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import TemplateView

from frontend.models import Booking
from frontend.models import Car


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)

        cars = Car.objects.filter(is_available=True)
        ctx['cars'] = cars

        return ctx


class CarDetailsView(DetailView):
    template_name = 'car_details.html'
    model = Car

    def get_context_data(self, **kwargs):
        ctx = super(CarDetailsView, self).get_context_data(**kwargs)
        ctx['booking_success'] = 'booking-success' in self.request.GET

        return ctx


class NewBookingView(CreateView):
    model = Booking
    fields = [
        'customer_name', 'customer_email', 'customer_phone_number',
        'booking_start_date', 'booking_end_date', 'booking_message'
    ]

    template_name = 'new_booking.html'

    def get_car(self):
        car_pk = self.kwargs['car_pk']
        car = Car.objects.get(pk=car_pk)

        return car

    def get_context_data(self, **kwargs):
        ctx = super(NewBookingView, self).get_context_data(**kwargs)
        ctx['car'] = self.get_car()

        return ctx

    def form_valid(self, form):
        new_booking = form.save(commit=False)
        new_booking.car = self.get_car()
        new_booking.is_approved = False

        new_booking.save()

        return super(NewBookingView, self).form_valid(form)

    def get_success_url(self):
        car = self.get_car()
        car_details_page_url = car.get_absolute_url()

        return '{}?booking-success=1'.format(car_details_page_url)
