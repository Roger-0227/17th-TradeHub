# Generated by Django 5.1.1 on 2024-09-20 19:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_id", models.CharField(max_length=20)),
                ("company_name", models.CharField(max_length=30)),
                ("gui_number", models.CharField(max_length=8, unique=True)),
                ("address", models.CharField(default="", max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        default=0,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="company",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
