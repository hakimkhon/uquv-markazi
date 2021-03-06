# Generated by Django 3.1.4 on 2022-03-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agent',
            old_name='profil',
            new_name='organisation',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_ustoz',
            field=models.BooleanField(default=False),
        ),
    ]
