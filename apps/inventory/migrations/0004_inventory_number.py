# Generated by Django 5.1.1 on 2024-09-22 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("inventory", "0003_merge_20240921_1837"),
    ]

    operations = [
        migrations.AddField(
            model_name="inventory",
            name="number",
            field=models.CharField(default=0, max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
