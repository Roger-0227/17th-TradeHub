# Generated by Django 5.1.1 on 2024-09-21 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clients", "0003_alter_client_state"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="client",
            name="delete_at",
        ),
        migrations.AddField(
            model_name="client",
            name="deleted_at",
            field=models.DateTimeField(null=True),
        ),
    ]
