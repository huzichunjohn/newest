# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ipaddr

from django.db import models
from django.core.exceptions import ValidationError

DEFAULT_EXPIRE = 7200     # 2 hour
DEFAULT_RETRY = 3600      # 1 hour
DEFAULT_REFRESH = 604800  # 1 week
DEFAULT_MINIMUM = 86400   # 1 day

class Line(models.Model):
    DEFAULT = 'DEFAULT'
    CNC = 'CNC'
    CT = 'CT'
    CMCC = 'CMCC'
    EDU = 'EDU'

    LINE_CHOICES = (
        (DEFAULT, '默认'),
        (CNC, '网通'),
	(CT, '电信'),
	(CMCC, '移动'),
	(EDU, '教育网')
    )

    description = models.CharField(max_length=20, choices=LINE_CHOICES, default=DEFAULT)

    class Meta: 
        db_table = 'line'

    def __unicode__(self):
        return self.description

class Domain(models.Model):
    name = models.CharField(max_length=50)
    line = models.ManyToManyField(Line)

class SOA(models.Model):
    primary = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    serial = models.PositiveIntegerField(
        null=False, default=2016072701)
    expire = models.PositiveIntegerField(null=False, default=DEFAULT_EXPIRE)
    retry = models.PositiveIntegerField(null=False, default=DEFAULT_RETRY)
    refresh = models.PositiveIntegerField(null=False, default=DEFAULT_REFRESH)
    minimum = models.PositiveIntegerField(null=False, default=DEFAULT_MINIMUM)
    domain = models.ForeignKey(Domain, related_name='soa')    

    class Meta:
        db_table = 'soa'

    @property
    def rdtype(self):
        return 'SOA'


    def render(self):
        return ("$TTL 86400\n"
                "@\t\tIN\t{0:5}\t{1:<20}\t{2:20} (\n"
                "\t\t\t\t{3:<20}\n"
                "\t\t\t\t{4:<20}\n"
                "\t\t\t\t{5:<20} \n"
                "\t\t\t\t{6})\n").format(
               self.rdtype, self.primary, self.contact, self.expire, self.retry,
               self.refresh, self.minimum)

class A(models.Model):
    name = models.CharField(max_length=50)
    ip = models.GenericIPAddressField()
    ttl = models.CharField(max_length=20, blank=True, default='')
    domain = models.ForeignKey(Domain, related_name='a')

    class Meta:
        db_table = 'a'

    @property
    def rdtype(self):
	return 'A'

    def render(self):
        return "{0:<15} IN\t{2:<5}\t{3:20}\n".format(self.name, self.ttl, self.rdtype, self.ip)

    def save(self, *args, **kwargs):
	super(A, self).save(*args, **kwargs)

class CNAME(models.Model):
    name = models.CharField(max_length=50)
    cname = models.CharField(max_length=50)
    domain = models.ForeignKey(Domain, related_name='cname')    

    class Meta:
        db_table = 'cname'

    @property
    def rdtype(self):
        return 'CNAME'

    def render(self):
        return "{0:<15} IN\t{1:<5}\t{2:<10}\n".format(self.name, self.rdtype, self.cname)

    def save(self, *args, **kwargs):
        super(CNAME, self).save(*args, **kwargs)

class TXT(models.Model):
    name = models.CharField(max_length=50)
    content = models.CharField(max_length=100)
    domain = models.ForeignKey(Domain, related_name='txt')

    class Meta:
        db_table = 'txt'

    @property
    def rdtype(self):
        return 'TXT'

    def render(self):
        return "{0:<15} IN\t{1:<5}\t\"{2:<8}\"".format(self.name, self.rdtype, self.content)

class NS(models.Model):
    name = models.CharField(max_length=50)
    domain = models.ForeignKey(Domain, related_name='ns')
    
    class Meta:
        db_table = 'ns'

    @property
    def rdtype(self):
        return 'NS'

    def render(self):
        return ("\t\tIN\t{0:<5}\t{1:20}\n").format(self.rdtype, self.name)

class MX(models.Model):
    name = models.CharField(max_length=50)
    domain = models.ForeignKey(Domain, related_name='mx')
    priority = models.PositiveIntegerField(null=False, default=10)

    class Meta:
        db_table = 'mx'

    @property
    def rdtype(self):
        return 'MX'

    def render(self):
        return ("\t\tIN\t{0:<5}\t{1:<5} {2:<10}\n").format(self.rdtype, self.priority, self.name)

