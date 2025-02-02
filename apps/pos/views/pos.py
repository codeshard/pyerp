# Librerias Django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView

# Librerias en carpetas locales
from ..models.pos import PyPos

POS_FIELDS = [
            {'string': 'Nombre', 'field': 'name'},
        ]

POS_FIELDS_SHORT = ['name']


class PosListView(LoginRequiredMixin, ListView):
    model = PyPos
    template_name = 'base/list.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PosListView, self).get_context_data(**kwargs)
        context['title'] = 'Puntos de Ventas'
        context['detail_url'] = 'base:pos-detail'
        context['add_url'] = 'base:pos-add'
        context['fields'] = POS_FIELDS
        return context

class PosDetailView(LoginRequiredMixin, DetailView):
    model = PyPos
    template_name = 'base/detail.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PosDetailView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:pos', 'name': 'Punto de Venta'}]
        context['update_url'] = 'base:pos-update'
        context['delete_url'] = 'base:pos-delete'
        context['fields'] = POS_FIELDS
        return context

class PosCreateView(LoginRequiredMixin, CreateView):
    model = PyPos
    fields = POS_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PosCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Crear Puntos de Venta'
        context['breadcrumbs'] = [{'url': 'base:pos', 'name': 'Punto de Venta'}]
        context['back_url'] = reverse('base:pos')
        return context

class PosUpdateView(LoginRequiredMixin, UpdateView):
    model = PyPos
    fields = POS_FIELDS_SHORT
    template_name = 'base/form.html'
    login_url = "login"

    def get_context_data(self, **kwargs):
        context = super(PosUpdateView, self).get_context_data(**kwargs)
        context['title'] = context['object'].name
        context['breadcrumbs'] = [{'url': 'base:pos', 'name': 'Punto de Venta'}]
        context['back_url'] = reverse('base:pos-detail', kwargs={'pk': context['object'].pk})
        return context


@login_required(login_url="base:login")
def DeletePos(self, pk):
    pos = PyPos.objects.get(id=pk)
    pos.delete()
    return redirect(reverse('base:pos'))
