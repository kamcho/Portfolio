from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView,TemplateView


from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactForm
from django.views.generic import TemplateView


class Home(FormView):
    template_name = 'Site/index.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Calls the custom send method
        form.send()
        return super().form_valid(form)


# class ContactView(FormView):
#     template_name = 'Site/index.html'
#     form_class = ContactForm
#     success_url = reverse_lazy('home')

#     def form_valid(self, form):
#         # Calls the custom send method
#         form.send()
#         return super().form_valid(form)
