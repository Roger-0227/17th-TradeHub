# Generated by Django 5.1.1 on 2024-09-21 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0008_alter_customuser_is_superuser_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="first_login",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="last_login",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="last login"
            ),
        ),
    ]
