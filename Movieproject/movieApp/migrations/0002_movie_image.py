# Generated by Django 4.1.3 on 2022-11-19 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='ddd', upload_to='pics'),
            preserve_default=False,
        ),
    ]