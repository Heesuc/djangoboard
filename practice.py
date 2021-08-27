from django.urls.resolvers import get_resolver
from board.models import Board
import graphene
from graphene.types import schema
from datetime import datetime

import json

class Query(graphene.ObjectType):
    is_staff = graphene.Boolean()

    def resolve_is_staff(self, info):
        return True

schema = graphene.Schema(query=Query)

result = schema.execute(
    '''
    {
        isStaff
    }
    '''
)

print(result.data.items())

item = dict(result.data.items())
print(json.dumps(item, indent=4))


class Board(graphene.ObjectType):
    bno = graphene.ID()
    btitle = graphene.String()
    bdate = graphene.DateTime()

class Query(graphene.ObjectType):
    boards = graphene.List(Board)

    def resolve_boards(self, info):
        return [
            Board(btitle='Title 1 입니다.', bdate=datetime.now()),
            Board(btitle='Title 2 입니다.', bdate=datetime.now()),
            Board(btitle='Title 3 입니다.', bdate=datetime.now())
        ]
    
schema = graphene.Schema(query=Query)

result1 = schema.execute(
    '''
    {
        boards {
            btitle
            bdate
        }
    }
    '''
)

print(result1)