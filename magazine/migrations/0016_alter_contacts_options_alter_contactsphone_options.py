# Generated by Django 4.1.4 on 2022-12-31 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0015_alter_logo_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contacts',
            options={'verbose_name': 'Контакты', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='contactsphone',
            options={'verbose_name': 'Телефоны', 'verbose_name_plural': 'Телефоны'},
        ),
    ]