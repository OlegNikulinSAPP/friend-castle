from django.db import models


class Friend(models.Model):
    # Основные поля
    name = models.CharField(max_length=100, verbose_name='Имя')
    age = models.IntegerField(verbose_name='Возраст', blank=True, null=True)
    is_close = models.BooleanField(default=False, verbose_name='Близкий друг')
    meeting_date = models.DateField(verbose_name='Дата знакомства', blank=True, null=True)
    notes = models.TextField(verbose_name='Заметки', blank=True)

    # Служебные поля (автоматически заполняются)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return self.name
