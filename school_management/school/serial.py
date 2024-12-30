# filepath: /c:/Users/Admin/Desktop/exonect/school_management/school/serializers.py
from rest_framework import serializers
from .models import Student, Teacher, Course

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'