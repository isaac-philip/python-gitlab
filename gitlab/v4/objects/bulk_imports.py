from gitlab.base import RESTManager, RESTObject
from gitlab.mixins import CreateMixin, ListMixin, RefreshMixin, RetrieveMixin
from gitlab.types import RequiredOptional

__all__ = [
    "BulkImport",
    "BulkImportManager",
    "BulkImportAllEntity",
    "BulkImportAllEntityManager",
    "BulkImportEntity",
    "BulkImportEntityManager",
]


class BulkImport(RefreshMixin, RESTObject):
    entities: "BulkImportEntityManager"


class BulkImportManager(CreateMixin, RetrieveMixin, RESTManager):
    _path = "/bulk_imports"
    _obj_cls = BulkImport
    _create_attrs = RequiredOptional(required=("configuration", "entities"))
    _list_filters = ("sort", "status")


class BulkImportEntity(RefreshMixin, RESTObject):
    pass


class BulkImportEntityManager(RetrieveMixin, RESTManager):
    _path = "/bulk_imports/{bulk_import_id}/entities"
    _obj_cls = BulkImportEntity
    _from_parent_attrs = {"bulk_import_id": "id"}
    _list_filters = ("sort", "status")


class BulkImportAllEntity(RESTObject):
    pass


class BulkImportAllEntityManager(ListMixin, RESTManager):
    _path = "/bulk_imports/entities"
    _obj_cls = BulkImportAllEntity
    _list_filters = ("sort", "status")
