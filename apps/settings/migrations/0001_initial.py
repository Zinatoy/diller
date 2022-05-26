# Generated by Django 4.0.4 on 2022-05-17 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Toyota', max_length=255, verbose_name='Название')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
                ('address', models.CharField(help_text='Ош', max_length=255, verbose_name='Адрес')),
                ('tel', models.CharField(help_text='+996772343206', max_length=255, verbose_name='Телефонный номер')),
                ('work_time', models.CharField(help_text='09:00 - 20:00 ПН-ПТ', max_length=255, verbose_name='Время работы')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
