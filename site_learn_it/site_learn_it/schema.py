import graphene

from learn_it.schema import Query as LearnItQuery
from learn_it.schema import Mutation as LearnItMutation

class Query(LearnItQuery, graphene.ObjectType):
    pass


class Mutation(LearnItMutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)