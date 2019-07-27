import graphene

from graphene_django import DjangoObjectType

from .models import Class, Student


class ClassType(DjangoObjectType):
    class Meta:
        model = Class


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(object):
    all_classes = graphene.List(ClassType)
    all_students = graphene.List(StudentType)


    def resolve_all_classes(self, info, **kwargs):
        return Class.objects.all()

    def resolve_all_students(self, info, **kwargs):
        return Student.objects.select_related('std_class').all()