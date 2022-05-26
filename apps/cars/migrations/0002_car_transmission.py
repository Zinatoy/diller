# Generated by Django 4.0.4 on 2022-05-19 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.ForeignKey(default=1, help_text='МЕХАНИКА', on_delete=django.db.models.deletion.CASCADE, to='cars.transmission', verbose_name='КОРОБКА ПЕРЕДАЧ'),
            preserve_default=False,
        ),
    ]
