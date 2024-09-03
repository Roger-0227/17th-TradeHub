# Generated by Django 5.1 on 2024-09-03 02:46

import datetime

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="supplier",
            old_name="contact",
            new_name="contact_person",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="GUInumber",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="remark",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="tel",
        ),
        migrations.AddField(
            model_name="supplier",
            name="email",
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="supplier",
            name="established_date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="supplier",
            name="gui_number",
            field=models.CharField(blank=True, max_length=8, unique=True),
        ),
        migrations.AddField(
            model_name="supplier",
            name="note",
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name="supplier",
            name="telephone",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="address",
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="name",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
