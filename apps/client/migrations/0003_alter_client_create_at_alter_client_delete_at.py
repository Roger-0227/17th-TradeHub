# Generated by Django 5.1 on 2024-08-28 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("client", "0002_alter_client_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="create_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="client",
            name="delete_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
