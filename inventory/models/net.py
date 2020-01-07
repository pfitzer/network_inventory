from django.db import models
from customer.models import Customer
from .category import Category


class IpStatus(Category):

    class Meta:
        verbose_name_plural = "IP Status"
        verbose_name = "IP Status"


class Net(models.Model):
    name = models.CharField(max_length=50)
    ip_range = models.CharField(max_length=50, verbose_name='IP Range')
    dhcp_range = models.CharField(max_length=50, verbose_name='DHCP Range')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('net', args=[str(self.id)])