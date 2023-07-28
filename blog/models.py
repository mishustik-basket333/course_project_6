from django.db import models

from users.models import NULLABLE


# Create your models here.
class Blog(models.Model):
    heading = models.CharField(max_length=150, verbose_name='заголовок')
    description = models.TextField(verbose_name='содержимое', **NULLABLE)
    picture = models.ImageField(upload_to='blog/', verbose_name='изображение', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создан', **NULLABLE)
    publication_flag = models.BooleanField(default=True, verbose_name='публикация')
    count_views = models.IntegerField(default=0, verbose_name='кол-во просмотров')

    def counter(self):
        self.count_views += 1
        self.save()

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.heading}'

    def delete(self, *args, **kwargs):
        self.publication_flag = False
        self.save()

    class Meta:
        verbose_name = 'публикация'  # Настройка для наименования одного объекта
        verbose_name_plural = 'публикации'  # Настройка для наименования набора объектов
        ordering = ('heading',)  # Сортировка по заголовку