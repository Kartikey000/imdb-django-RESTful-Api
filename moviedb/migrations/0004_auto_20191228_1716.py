# Generated by Django 2.2.8 on 2019-12-28 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviedb', '0003_auto_20191228_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Director',
        ),
    ]
