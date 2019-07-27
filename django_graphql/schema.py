import graphene

import student.schema


class Query(student.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple query
    pass


schema = graphene.Schema(query=Query)