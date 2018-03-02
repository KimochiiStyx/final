# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
# Register your models here.
from django.contrib.auth.models import Course, Group, Curriculum, Implementation, ImplementationGroup, ImplementationTeacher, Teacher

admin.site.register(Course)
admin.site.register(Curriculum)
admin.site.register(Group)
admin.site.register(Implementation)
admin.site.register(ImplementationGroup)
admin.site.register(ImplementationTeacher)
admin.site.register(Teacher)