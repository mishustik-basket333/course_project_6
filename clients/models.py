from datetime import datetime
from django.db import models
from users.models import NULLABLE, User


# Класс клиенты
class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='почта')
    name = models.CharField(max_length=250, verbose_name='имя')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.email} {self.name}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


# Класс рассылка
class Mailings(models.Model):

    PERIOD_CHOICES = (
        ('день', 'день'),
        ('неделя', 'неделя'),
        ('месяц', 'месяц')
    )
    STATUS_CHOICES = (
        ('создано', 'создано'),
        ('в процессе', 'в процессе'),
        ('завершено', 'завершено'),
    )

    time = models.TimeField(**NULLABLE, verbose_name='время', default=datetime.now().time())
    date = models.DateField(verbose_name='дата', auto_now=True)
    period = models.CharField(max_length=20, choices=PERIOD_CHOICES, verbose_name='Период отправки')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='создано',
                              verbose_name='Статус рассылки')
    clients = models.ManyToManyField(Client, verbose_name='Принадлежит к клиенту:')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.time}, {self.status}, {self.clients}'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'
        ordering = ('-date',)


# Класс сообщение
class Mail(models.Model):
    subject = models.CharField(max_length=500, verbose_name='Заголовок сообщения')
    body = models.TextField(verbose_name='Тело сообщения')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    mailings = models.ForeignKey(Mailings, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

    def __str__(self):
        return f'{self.subject}'


# Класс логов
class Log(models.Model):

    STATUS_CHOICES = (
        ('завершено', 'завершено'),
        ('неудачно', 'неудачно'),
    )

    last_q = models.DateTimeField(auto_now_add=True, verbose_name='попытка отправления')
    status = models.CharField(max_length=25, choices=STATUS_CHOICES,
                              verbose_name='статус')
    answer_server = models.BooleanField(verbose_name='ответ сервера')
    mailing = models.ForeignKey(Mailings, on_delete=models.CASCADE, verbose_name="рассылка")

    class Meta:
        verbose_name = 'Лог'
        verbose_name_plural = 'Логи'
