import graphene
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from falmer.content.models import name_to_class_map, all_pages
from falmer.content.utils import get_public_path_for_page


class PageResult(graphene.ObjectType):
    content_type = graphene.String()

    title = graphene.String()
    slug = graphene.String()

    seo_title = graphene.String()
    search_description = graphene.String()

    last_published_at = graphene.DateTime()

    url_path = graphene.String()
    path = graphene.String()

    data = GenericScalar()

    id = graphene.Int()

    def resolve_content_type(self, info):
        return self.__class__.__name__

    def resolve_title(self, info):
        return self.title

    def resolve_slug(self, info):
        return self.slug

    def resolve_seo_title(self, info):
        return self.seo_title

    def resolve_search_description(self, info):
        return self.search_description

    def resolve_last_published_at(self, info):
        return self.last_published_at

    def resolve_url_path(self, info):
        return self.url_path

    def resolve_id(self, info):
        return self.pk

    def resolve_path(self, info):
        return self.public_path


class Page(graphene.Interface):
    content_type = graphene.String()

    title = graphene.String()
    slug = graphene.String()

    seo_title = graphene.String()
    search_description = graphene.String()

    last_published_at = graphene.DateTime()

    url_path = graphene.String()
    path = graphene.String()

    sub_pages = graphene.List(lambda: Page, in_menu=graphene.Boolean())
    sibling_pages = graphene.List(lambda: Page, in_menu=graphene.Boolean())
    parent_page = graphene.Field(lambda: Page)
    ancestor_pages = graphene.List(lambda: Page, in_menu=graphene.Boolean())
    closest_ancestor_of_type = graphene.Field(lambda: Page, content_type=graphene.String(), inclusive=graphene.Boolean())

    def resolve_content_type(self, info):
        return self.__class__.__name__

    def resolve_title(self, info):
        return self.title

    def resolve_slug(self, info):
        return self.slug

    def resolve_seo_title(self, info):
        return self.seo_title

    def resolve_search_description(self, info):
        return self.search_description

    def resolve_last_published_at(self, info):
        return self.last_published_at

    def resolve_url_path(self, info):
        return self.url_path

    def resolve_path(self, info):
        if hasattr(self, 'public_path'):
            return self.public_path
        else:
            return get_public_path_for_page(self)

    def resolve_parent_page(self, info):
        return self.get_parent().specific

    def resolve_sub_pages(self, info, in_menu=None):
        q = self.get_children().specific().live()
        if in_menu is True:
            q = q.in_menu()

        return q

    def resolve_sibling_pages(self, info, in_menu=None):
        q = self.get_siblings().specific().live()

        if in_menu is True:
            q = q.in_menu()

        return q

    def resolve_ancestor_pages(self, info, in_menu=None):
        q = self.get_ancestors().specific().live()

        if in_menu is True:
            q = q.in_menu()

        return q

    def resolve_closest_ancestor_of_type(self, info, content_type=None, inclusive=False):
        try:
            return self.get_ancestors(inclusive).type(name_to_class_map[content_type]).last()
        except IndexError:
            return None

    @classmethod
    def resolve_type(cls, instance, info):
        name = instance.__class__.__name__
        if name in page_types_map:
            return page_types_map[name]

        return GenericPage


def generate_interfaces_for_type(page_models):
    types = {}

    for page in page_models:
        meta = type('Meta', (), {
            'interfaces': (Page, ),
            'model': page,
        })
        types[page.__name__] = type(page.__name__, (DjangoObjectType, ), {
            'Meta': meta
        })

    return types


page_types_map = generate_interfaces_for_type(all_pages)


class GenericPage(graphene.ObjectType):
    class Meta:
        interfaces = (Page, )
