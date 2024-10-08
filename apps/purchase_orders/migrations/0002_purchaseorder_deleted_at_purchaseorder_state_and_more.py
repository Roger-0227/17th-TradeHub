# Generated by Django 5.1.1 on 2024-09-17 06:05

import django.db.models.deletion
import django_fsm
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
        ("purchase_orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="purchaseorder",
            name="deleted_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="state",
            field=django_fsm.FSMField(
                choices=[("unfinish", "未完成"), ("finished", "完成")],
                default="unfinish",
                max_length=50,
                protected=True,
            ),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="order_number",
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name="purchaseorder",
            name="supplier_email",
            field=models.EmailField(max_length=254),
        ),
        migrations.CreateModel(
            name="ProductItem",
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
                ("quantity", models.PositiveIntegerField()),
                ("cost_price", models.PositiveIntegerField()),
                ("subtotal", models.PositiveIntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
                (
                    "purchase_order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="purchase_orders.purchaseorder",
                    ),
                ),
            ],
        ),
    ]
