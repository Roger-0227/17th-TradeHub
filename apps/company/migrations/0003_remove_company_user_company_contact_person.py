# Generated by Django 5.1.1 on 2024-09-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0002_alter_company_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="company", name="user",),
        migrations.AddField(
            model_name="company",
            name="contact_person",
            field=models.CharField(default="", max_length=20),
        ),
    ]
