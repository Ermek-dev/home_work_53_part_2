# Generated by Django 5.0.3 on 2024-03-19 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('status', models.CharField(choices=[('NEW', 'Новая'), ('IN_PROCESSING', 'В процессе'), ('DONE', 'Сделано')], default='NEW', max_length=20, verbose_name='Статус')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата выполнения')),
            ],
        ),
    ]
