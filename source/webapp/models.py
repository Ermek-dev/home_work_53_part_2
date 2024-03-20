from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = 'NEW', 'Новая'
    IN_PROCESSING = 'IN_PROCESSING','В процессе'
    DONE = 'DONE', 'Сделано'
class Article(models.Model):
    title = models.CharField(max_length=200, null = False, blank = False, verbose_name = 'Заголовок')
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.NEW)
    created_at = models.DateTimeField( auto_now_add=True,  verbose_name='Дата выполнения')



    def __str__(self):
        return f'{self.title} - {self.description}'