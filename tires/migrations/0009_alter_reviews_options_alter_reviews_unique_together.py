# Generated by Django 4.2.9 on 2024-04-15 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tires', '0008_favorite_user_alter_favorite_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviews',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together=set(),
        ),
    ]