from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

class Blog(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField()
    owner = models.ForeignKey(User)

    class Meta:
	db_table = u'blog'

    def __unicode__(self):
	return u'%s %s' % (self.title, self.owner.username)

class Author(models.Model):
    name = models.CharField(max_length=200)
    last_accessed = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
	return reverse('author-detail', kwargs={'pk': self.pk})
