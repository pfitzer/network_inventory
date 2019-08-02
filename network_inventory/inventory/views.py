from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from guardian.shortcuts import get_objects_for_user
from django_tables2 import RequestConfig
from .decorators import computer_view_permission
from .models import (Device, Computer, ComputerRamRelation,
                     ComputerDiskRelation, ComputerCpuRelation,
                     ComputerSoftwareRelation, Customer, Net, RaidInComputer,
                     Backup)
from .tables import CustomersTable, ComputersTable, DevicesTable, NetsTable, NetDetailTable, BackupDetailTable


def device_detail_view(request, device_id):
    device = get_object_or_404(Device, pk=device_id)
    return render(request, 'inventory/device_details.html',
                  {'device': device})


@login_required
@computer_view_permission
def computer_detail_view(request, computer_id):
    computer = get_object_or_404(Computer, pk=computer_id)
    disks_list = ComputerDiskRelation.objects.filter(computer=computer_id)
    ram_list = ComputerRamRelation.objects.filter(computer=computer_id)
    cpu_list = ComputerCpuRelation.objects.filter(computer=computer_id)
    software_list = ComputerSoftwareRelation.objects.filter(computer=computer_id)
    raid_relations = RaidInComputer.objects.filter(computer=computer_id)
    raid_relations = RaidInComputer.objects.filter(computer=computer_id)
    backup_list = Backup.objects.filter(computer=computer_id)
    context = {'computer': computer,
               'disks_list': disks_list,
               'ram_list': ram_list,
               'cpu_list': cpu_list,
               'software_list': software_list,
               'raid_relations': raid_relations,
               'backup_list': backup_list }
    return render(request, 'inventory/computer_details.html', context)


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'inventory/customer_details.html'


def customers_table_view(request):
    table = CustomersTable(
        get_objects_for_user(request.user,
                             'inventory.view_customer',
                             klass=Customer))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/customer_list.html', {'customers': table})


def computers_table_view(request, customer_id):
    table = ComputersTable(Computer.objects.filter(customer=customer_id))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/computer_list.html', {'computers': table})


def devices_table_view(request, customer_id):
    table = DevicesTable(Device.objects.filter(customer=customer_id))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/device_list.html', {'devices': table})


def nets_table_view(request, customer_id):
    table = NetsTable(Net.objects.filter(customer=customer_id))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/net_list.html', {'nets': table})


def net_detail_view(request, pk):
    table = NetDetailTable(Net.objects.filter(pk=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/net_details.html', {'net': table})


def backup_detail_view(request, pk):
    table = BackupDetailTable(Backup.objects.filter(pk=pk))
    RequestConfig(request).configure(table)
    return render(request, 'inventory/backup_details.html', {'backup': table})
