from django.db import models
from .cpu import Cpu
from .devices import ConnectedDevice
from .disk import Disk
from .os import OperatingSystem
from .raid import RaidType, DisksInRaid
from .ram import Ram
from .software import Software, SoftwareArchitecture


class Computer(ConnectedDevice):
    os = models.ForeignKey(OperatingSystem, models.SET_NULL, blank=True,
                           null=True)
    cpu = models.ManyToManyField(Cpu, through='ComputerCpuRelation')
    ram = models.ManyToManyField(Ram, through='ComputerRamRelation')
    disks = models.ManyToManyField(Disk, through='ComputerDiskRelation')
    software = models.ManyToManyField(Software,
                                      through='ComputerSoftwareRelation')
    host = models.ForeignKey('self', null=True, blank=True,
                             on_delete=models.CASCADE)
    allocated_space = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['name']


class ComputerCpuRelation(models.Model):
    cpu = models.ForeignKey(Cpu, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.computer.name

    class Meta:
        verbose_name_plural = "CPUs in Computer"


class ComputerRamRelation(models.Model):
    ram = models.ForeignKey(Ram, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.computer.name

    class Meta:
        verbose_name_plural = "RAM Modules in Computer"


class ComputerDiskRelation(models.Model):
    disk = models.ForeignKey(Disk, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.computer.name

    class Meta:
        verbose_name_plural = "Disks in Computer"


class RaidInComputer(models.Model):
    disks = models.ForeignKey(DisksInRaid, models.SET_NULL, blank=True,
                              null=True)
    usable_space = models.IntegerField(blank=True, null=True)
    raid_type = models.ForeignKey(RaidType, models.SET_NULL, blank=True,
                                  null=True)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)

    def __str__(self):
        return self.computer.name

    class Meta:
        verbose_name_plural = "RAIDs in Computer"


class ComputerSoftwareRelation(models.Model):
    software = models.ForeignKey(Software, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    architecture = models.ForeignKey(SoftwareArchitecture, models.SET_NULL,
                                     blank=True, null=True)

    def __str__(self):
        return self.computer.name

    class Meta:
        verbose_name_plural = "Software on Computer"