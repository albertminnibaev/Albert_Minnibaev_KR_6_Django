from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from service.forms import ClientForm, MailingForm, MessageForm
from service.models import Client, Mailing, Message, Logs
from service.services import start_1
from services import send_order_email


class IndexView(TemplateView):
    template_name = 'service/index.html'
    extra_context = {
        "title": 'Главная'
    }


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов'
    }

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    #fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('service:client')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    #fields = ('name', 'email', 'comment')
    success_url = reverse_lazy('service:client')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user:
            raise Http404
        return self.object

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('service:client')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        return super().get_queryset().filter(creator=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    #fields = ('time', 'frequency', 'status', 'message', 'client')
    success_url = reverse_lazy('service:mailing')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.creator != self.request.user:
            raise Http404
        return self.object

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        #send_order_email(obj)
        start_1(self.object)
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    form_class = MailingForm
    #fields = ('time', 'frequency', 'status', 'message', 'client')
    success_url = reverse_lazy('service:mailing')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        #send_order_email(obj)
        start_1(self.object)
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    success_url = reverse_lazy('service:mailing')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Список сообщений'
    }


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('service:message')


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('service:message')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    success_url = reverse_lazy('service:message')


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs
    extra_context = {
        'title': 'Отчеты о проведенных рассылка'
    }
