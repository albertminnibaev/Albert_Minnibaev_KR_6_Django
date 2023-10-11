from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.cache import cache
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView

from blog.models import Article
from config import settings
from service.forms import ClientForm, MailingForm, MessageForm
from service.models import Client, Mailing, Message, Logs
from service.services import start_1
from services import send_order_email


class IndexView(TemplateView):
    template_name = 'service/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Главная'
        context['count_mailing'] = Mailing.objects.all().count()
        context['count_activ_mailing'] = Mailing.objects.all().filter(status='создана').count()
        context['count_client'] = Client.objects.all().distinct().count()
        if settings.CACHE_ENABLED:
            key = 'article_list'
            article_list = cache.get(key)
            if article_list is None:
                article_list = Article.objects.all()
                cache.set(key, article_list)
            context['random_article'] = article_list.order_by('?')[:3]
        else:
            context['random_article'] = Article.objects.all().order_by('?')[:3]
        return context


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    extra_context = {
        'title': 'Список клиентов'
    }
    #permission_required = 'service.view_client'

    def get_queryset(self):
        object = super().get_queryset()
        if not self.request.user.is_superuser:
            object = object.filter(creator=self.request.user)
        return object


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    form_class = ClientForm
    #permission_required = 'service.add_client'
    success_url = reverse_lazy('service:client')

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        self.object.save()

        return super().form_valid(form)


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    form_class = ClientForm
    #permission_required = 'service.change_client'
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
    #permission_required = 'service.view_client'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    #permission_required = 'service.delete_client'
    success_url = reverse_lazy('service:client')


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    #permission_required = 'service.view_mailing'
    extra_context = {
        'title': 'Список рассылок'
    }

    def get_queryset(self):
        if not self.request.user.is_staff:
            return super().get_queryset().filter(creator=self.request.user)
        return super().get_queryset()


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    form_class = MailingForm
    #permission_required = 'service.add_mailing'
    success_url = reverse_lazy('service:mailing')

    def get_form_kwargs(self):
        kwargs = super(MailingCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем текущего пользователя в форму
        return kwargs

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
    #permission_required = 'service.change_mailing'
    success_url = reverse_lazy('service:mailing')

    def get_form_kwargs(self):
        kwargs = super(MailingUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем текущего пользователя в форму
        return kwargs

    def form_valid(self, form):
        self.object = form.save()
        self.object.creator = self.request.user
        start_1(self.object)
        return super().form_valid(form)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    #permission_required = 'service.view_mailing'


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    #permission_required = 'service.delete_mailing'
    success_url = reverse_lazy('service:mailing')


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    extra_context = {
        'title': 'Список сообщений'
    }
    #permission_required = 'service.view_message'


class MessageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Message
    form_class = MessageForm
    permission_required = 'service.add_message'
    success_url = reverse_lazy('service:message')


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Message
    form_class = MessageForm
    permission_required = 'service.change_message'
    success_url = reverse_lazy('service:message')


class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    #permission_required = 'service.view_message'


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Message
    permission_required = 'service.delete_message'
    success_url = reverse_lazy('service:message')


class LogsListView(LoginRequiredMixin, ListView):
    model = Logs
    #permission_required = 'service.view_logs'
    extra_context = {
        'title': 'Отчеты о проведенных рассылка'
    }


def toggle_activity(request, pk):
    mailing_item = get_object_or_404(Mailing, pk=pk)
    if mailing_item.status == 'создана':
        mailing_item.status = 'завершена'
    else:
        mailing_item.status = 'создана'

    mailing_item.save()

    return redirect(reverse('service:mailing'))
