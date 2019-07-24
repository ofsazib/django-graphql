import graphene

from graphene_django import DjangoObjectType

from .models import Class, Student


class ClassType(DjangoOjectType):
    class Meta:
        model = Class


class StudentType(DjangoObjectType):
    class Meta:
        model = Student


class Query(object):
    hello = graphene.String()


    resolve_hello(self, info, **kwargs):
        return "world"