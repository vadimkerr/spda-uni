# Generated by Django 3.2.10 on 2021-12-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180616_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
