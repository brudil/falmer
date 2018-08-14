from graphene_django import DjangoObjectType

from . import models


class Banner(DjangoObjectType):
    class Meta:
        model = models.Banner
        only_fields = (
            'id',
            'outlet',
            'display_from',
            'display_to',
            'purpose',
            'heading',
            'body',
        )
