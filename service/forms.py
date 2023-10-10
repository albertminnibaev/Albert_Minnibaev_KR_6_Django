from django import forms

from service.models import Client, Mailing, Message


class StyleFromMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ClientForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('creator',)


class MailingForm(StyleFromMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) # Извлекаем пользователя из аргументов
        super(MailingForm, self).__init__(*args, **kwargs)

        # Ограничиваем queryset для выбора клиентов только теми, которых создал текущий пользователь
        self.fields['client'].queryset = Client.objects.filter(creator=user)

    class Meta:
        model = Mailing
        exclude = ('creator',)


class MessageForm(StyleFromMixin, forms.ModelForm):

    class Meta:
        model = Message
        fields = '__all__'


