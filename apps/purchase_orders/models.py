import re

from django.db import models
from django.utils import timezone

from apps.suppliers.models import Supplier


class PurchaseOrder(models.Model):
    order_number = models.CharField(max_length=10, unique=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name="purchase_orders"
    )
    supplier_tel = models.CharField(max_length=15)
    contact_person = models.CharField(max_length=20)
    supplier_email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.order_number:
            today = timezone.localtime().strftime("%Y%m%d")
            last_order = (
                PurchaseOrder.objects.filter(order_number__startswith=today)
                .order_by("order_number")
                .last()
            )
            if last_order:
                last_order_number = int(last_order.order_number[-3:])
                new_order_number = f"{last_order_number + 1:03d}"
            else:
                new_order_number = "001"
            self.order_number = f"{today}{new_order_number}"

        self.supplier_tel = self.format_supplier_tel(self.supplier_tel)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order_number} - {self.supplier.name}"

    def format_supplier_tel(self, number):
        # 把所有非數字符號改為空字串(清除)
        number = re.sub(r"\D", "", number)

        # 將輸入的電話號碼格式化為 09XX-XXXXXX 或 0X-XXXXXXX
        if len(number) == 10 and number.startswith("09"):
            return f"{number[:4]}-{number[4:]}"
        elif len(number) == 9 and number.startswith("0"):
            return f"{number[:2]}-{number[2:]}"
        else:
            return number
