# Generated by Django 3.1.2 on 2020-11-07 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0004_auto_20201107_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forumuser',
            name='user',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='user',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ForumUser',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
