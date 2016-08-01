# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import ipaddr

from django.db import models
from django.core.exceptions import ValidationError

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
    expire = models.PositiveIntegerField(null=False, default=1)
    retry = models.PositiveIntegerField(null=False, default=2)
    refresh = models.PositiveIntegerField(null=False, default=3)
    minimum = models.PositiveIntegerField(null=False, default=4)
    domain = models.ForeignKey(Domain, related_name='soa')    

    class Meta:
        db_table = 'soa'

    @property
    def rdtype(self):
        return 'SOA'

    def render(self):
        return ("$ORIGIN {0}\n"
                "$TTL 86400\n"
                "@                    IN    {1:<10}    {2:<20}    {3:<10} (\n" 
                "                                      {4:20}              \n"
                "                                      {5:20}              \n"
                "                                      {6:20}              \n"
                "                                      {7:20})             \n").format(
               self.domain.name, self.rdtype, self.primary, self.contact, self.expire, 
               self.retry, self.refresh, self.minimum)

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
        return "{0:<14} {1:<5} IN  {2:10} {3:<10}".format(self.name, self.ttl, self.rdtype, self.ip)

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
        return "{0}                 IN  {1:<10} {2:<10}".format(self.name, self.rdtype, self.cname)

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
        return "{0:<20} IN  {1:<10} \"{2:<10}\"".format(self.name, self.rdtype, self.content)

class NS(models.Model):
    name = models.CharField(max_length=50)
    domain = models.ForeignKey(Domain, related_name='ns')
    
    class Meta:
        db_table = 'ns'

    @property
    def rdtype(self):
        return 'NS'

    def render(self):
        return ("                     IN  {0:<10} {1:<10}").format(self.rdtype, self.name)

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
        return ("                     IN  {0:<10} {1:<10} {2:<10}").format(self.rdtype, self.name, self.priority)
