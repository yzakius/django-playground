# Generated by Django 2.2.2 on 2019-06-20 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_decks'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Decks',
            new_name='Deck',
        ),
    ]