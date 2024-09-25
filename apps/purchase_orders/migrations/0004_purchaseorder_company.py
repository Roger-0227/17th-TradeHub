# Generated by Django 5.1.1 on 2024-09-22 05:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("company", "0006_remove_company_company_id"),
        ("purchase_orders", "0003_rename_total_amount_purchaseorder_amount_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="company",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="purchase_orders",
                to="company.company",
            ),
        ),
    ]
