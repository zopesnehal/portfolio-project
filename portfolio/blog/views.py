# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from.models import Blog

def allblogs(request):

	blogs = Blog.objects
	return render(request, 'blog/allblogs.html',{'blogs':blogs})
 