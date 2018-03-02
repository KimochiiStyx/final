from django.contrib.auth.models import User
from models import Course, Group, Curriculum, Implementation, ImplementationGroup, ImplementationTeacher, Teacher
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email')

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ('url', 'code', 'credit', 'name', 'language', 'type', 'curriculumid')

class CurriculumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curriculum
        fields = ('url', 'name')
		
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'groupcode')		

class ImplementationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Implementation
        fields = ('url', 'courseid', 'p1', 'p2', 'p3', 'p4', 'p5')
		
class ImplementationGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementationGroup
        fields = ('url', 'implementationid', 'groupid')
		
class ImplementationTeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ImplementationTeacher
        fields = ('url', 'implementationid', 'teacherid')
		
class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'teacherid', 'firstname', 'surname')