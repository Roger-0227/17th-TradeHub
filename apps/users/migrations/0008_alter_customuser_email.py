# Generated by Django 5.1.1 on 2024-09-25 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_merge_0006_alter_customuser_options_0006_invitation"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
