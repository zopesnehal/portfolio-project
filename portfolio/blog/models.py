# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class job(models.model):	
	imagae = models.ImageField(upload='images/')
	summary = models.CharField(max_lenght=200)
 