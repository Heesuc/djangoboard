import graphene
from board.schema import BoardQuery

class Query(
    BoardQuery,
    ): 
    pass

schema = graphene.Schema(query=Query)