# Generated by Django 4.1.4 on 2023-01-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0019_alter_homeacademy_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.CharField(max_length=100, verbose_name='Почта')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Обращение клиентов',
                'verbose_name_plural': 'Обращения клиентов',
            },
        ),
    ]