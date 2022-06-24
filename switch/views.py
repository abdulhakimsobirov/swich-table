
from django.views.generic import ListView, DetailView 
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from requests import request
from .filters import SwitchFilter 
from .models import Switch
from .forms import SwitchForm
from django.shortcuts import render


class SwitchList(ListView): 
   
    model = Switch
    
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['filter'] = SwitchFilter(self.request.GET, queryset=self.get_queryset())
        return context


# def switchList(request):
#     # switch = Switch.objects.get(id=pk)

#     object_list = Switch.objects.all()
    
#     tfilter = SwitchFilter()
#     # switchf = tfilter.qs



#     context = {'object_list': object_list, 'tfilter': tfilter,}
#     return render(request, 'switch/switch_list.html', context)


class SwitchDetail(DetailView): 
    model = Switch

class SwitchCreate(SuccessMessageMixin, CreateView): 
    model = Switch
    form_class = SwitchForm
    success_url = reverse_lazy('switch_list')
    success_message = "Product successfully created!"

class SwitchUpdate(SuccessMessageMixin, UpdateView): 
    model = Switch
    form_class = SwitchForm
    success_url = reverse_lazy('switch_list')
    success_message = "Product successfully updated!"

class SwitchDelete(SuccessMessageMixin, DeleteView):
    model = Switch
    success_url = reverse_lazy('switch_list')
    success_message = "Product successfully deleted!"

def tableHower(request):
    return render(request,  'switch/table_hower.html')
