# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Blog(models.Model):
	title = models.CharField(max_length=255)
	pub_date = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')


