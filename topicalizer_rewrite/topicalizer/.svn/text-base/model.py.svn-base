from turbogears.database import PackageHub
from sqlobject import *

hub = PackageHub("topicalizer")
__connection__ = hub

class token_by_category(SQLObject):
    token = StringCol()
    category = StringCol()

class co_occurrence(SQLObject):
    token = StringCol()
    co_occurs_with = IntCol()
    count = IntCol()

class client(SQLObject):
    ip_address = StringCol()
    access_time = StringCol()
