# Generated by Django 5.1.1 on 2024-09-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_alter_game_options_alter_gamedetails_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(upload_to='img/', verbose_name='تصویر'),
        ),
    ]