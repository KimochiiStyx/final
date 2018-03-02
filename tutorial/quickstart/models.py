# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Course(models.Model):
    code = models.CharField(max_length=10)
    credit = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=5, blank=True, null=True)
    type = models.CharField(max_length=20, blank=True, null=True)
    curriculumid = models.ForeignKey('Curriculum', models.DO_NOTHING, db_column='curriculumid')

    class Meta:
        managed = False
        db_table = 'course'


class Curriculum(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'curriculum'


class Group(models.Model):
    groupcode = models.CharField(db_column='groupCode', unique=True, max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'


class Implementation(models.Model):
    courseid = models.ForeignKey(Course, models.DO_NOTHING, db_column='courseid')
    p1 = models.IntegerField(blank=True, null=True)
    p2 = models.IntegerField(blank=True, null=True)
    p3 = models.IntegerField(blank=True, null=True)
    p4 = models.IntegerField(blank=True, null=True)
    p5 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'implementation'


class ImplementationGroup(models.Model):
    implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid', primary_key=True)
    groupid = models.ForeignKey(Group, models.DO_NOTHING, db_column='groupid')

    class Meta:
        managed = False
        db_table = 'implementation_group'
        unique_together = (('implementationid', 'groupid'),)


class ImplementationTeacher(models.Model):
    implementationid = models.ForeignKey(Implementation, models.DO_NOTHING, db_column='implementationid', primary_key=True)
    teacherid = models.ForeignKey('Teacher', models.DO_NOTHING, db_column='teacherid')

    class Meta:
        managed = False
        db_table = 'implementation_teacher'
        unique_together = (('implementationid', 'teacherid'),)


class Teacher(models.Model):
    teacherid = models.CharField(db_column='teacherID', unique=True, max_length=10)  # Field name made lowercase.
    firstname = models.CharField(max_length=45)
    surname = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'teacher'
