from django.db import models


class Hobby(models.Model):
    """Модель увлечения (хобби) друзей"""
    name = models.CharField(
        max_length=100,
        verbose_name="Название увлечения",
        help_text="Например: рисование, программирование, футбол"
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Подробное описание увлечения",
        blank=True,  # Может быть пустым
        null=True    # Может быть NULL в базе данных
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # Автоматически ставит текущую дату при создании
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Увлечение"
        verbose_name_plural = "Увлечения"
        ordering = ['name']  # Сортировка по названию

    def __str__(self):
        return self.name  # Как будет отображаться в админке


class Friend(models.Model):
    """Модель друга"""
    name = models.CharField(
        max_length=100,
        verbose_name="Имя друга"
    )
    email = models.EmailField(
        verbose_name="Email",
        unique=True,  # Email должен быть уникальным
        help_text="Уникальный email друга"
    )
    phone = models.CharField(
        max_length=20,
        verbose_name="Телефон",
        blank=True,  # Может быть пустым
        null=True
    )
    birth_date = models.DateField(
        verbose_name="Дата рождения",
        blank=True,
        null=True
    )
    # Связь "многие-ко-многим" с увлечениями
    hobbies = models.ManyToManyField(
        Hobby,
        related_name="friends",  # Как обращаться из Hobby к Friend
        verbose_name="Увлечения",
        blank=True  # Может не иметь увлечений
    )
    is_close_friend = models.BooleanField(
        default=False,
        verbose_name="Близкий друг"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Друг"
        verbose_name_plural = "Друзья"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.email})"


class Meeting(models.Model):
    """Модель встречи друзей"""
    title = models.CharField(
        max_length=200,
        verbose_name="Название встречи"
    )
    description = models.TextField(
        verbose_name="Описание встречи",
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=200,
        verbose_name="Место встречи"
    )
    date = models.DateTimeField(
        verbose_name="Дата и время встречи"
    )
    # Связь "многие-ко-многим" с друзьями
    participants = models.ManyToManyField(
        Friend,
        related_name="meetings",
        verbose_name="Участники"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Встреча"
        verbose_name_plural = "Встречи"
        ordering = ['-date']  # Сортировка по дате (новые сверху)

    def __str__(self):
        return f"{self.title} ({self.date.strftime('%d.%m.%Y')})"
