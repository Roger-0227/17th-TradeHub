import django.db.models.deletion
import django_fsm
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Inventory",
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
                ("safety_stock", models.PositiveIntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("delete_at", models.DateTimeField(auto_now=True)),
                ("last_updated", models.DateTimeField(auto_now=True)),
                ("note", models.TextField(blank=True)),
                (
                    "state",
                    django_fsm.FSMField(
                        choices=[
                            ("out_stock", "缺貨"),
                            ("low_stock", "低於安全庫存量"),
                            ("normal", "正常"),
                        ],
                        default="normal",
                        max_length=50,
                        protected=True,
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inventories",
                        to="products.product",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="inventories",
                        to="suppliers.supplier",
                    ),
                ),
            ],
        ),
    ]
