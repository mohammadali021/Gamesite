# Generated by Django 5.1.1 on 2024-09-27 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_game_image1_game_image2_game_image3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='file_size',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='حجم فایل'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='تصویر اول'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='تصویر دوم'),
        ),
        migrations.AlterField(
            model_name='game',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='تصویر سوم'),
        ),
        migrations.AlterField(
            model_name='game',
            name='long_description',
            field=models.TextField(blank=True, null=True, verbose_name='توضیحات کامل بازی'),
        ),
    ]