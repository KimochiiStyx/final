from django.contrib.auth.models import User
from models import Course, Group, Curriculum, Implementation, ImplementationGroup, ImplementationTeacher, Teacher
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, CourseSerializer, GroupSerializer, CurriculumSerializer, GroupSerializer, ImplementationSerializer, ImplementationGroupSerializer, ImplementationTeacherSerializer, TeacherSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
	
	
class CurriculumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
	
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class ImplementationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Implementation.objects.all()
    serializer_class = ImplementationSerializer
	
class ImplementationGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = ImplementationGroup.objects.all()
    serializer_class = ImplementationGroupSerializer
	
class ImplementationTeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = ImplementationTeacher.objects.all()
    serializer_class = ImplementationTeacherSerializer
	
class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows persons to be viewed or edited.
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer