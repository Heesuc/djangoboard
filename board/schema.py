import graphene
from graphene_django.types import DjangoObjectType
from .models import Board

class BoardType(DjangoObjectType):
    class Meta:
        model = Board

class BoardQuery(graphene.ObjectType):
    allBoard = graphene.List(BoardType)

    def resolve_allBoard(self, info, **kwargs):
        return Board.objects.all()


