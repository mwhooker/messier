import boto.regioninfo
import datetime

from collections import MutableMapping
from json import JSONEncoder, dumps
from time import mktime


def json_encoder(obj):
    if isinstance(obj, boto.regioninfo.RegionInfo):
        return obj.name
    elif isinstance(obj, datetime.datetime):
        return int(mktime(obj.timetuple()))

    return JSONEncoder.default(self, obj)


class Resource(MutableMapping):

    def __init__(self, Name=None, Type=None, encoder=json_encoder, **properties):
        self.name = Name

        self.__type__ = Type
        if not self.__type__:
            self.__type__ = self.__class__.__name__

        self.__encoder__ = encoder
        self.__store__ = dict()

        props = dict(**properties)
        del props["connection"]
        self.update(props)

    def __getitem__(self, key):
        return self.__store__[key]

    def __setitem__(self, key, value):
        self.__store__[key] = value

    def __delitem__(self, key):
        del self.__store__[key]

    def __iter__(self):
        return iter(self.__store__)

    def __len__(self):
        return len(self.__store__)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, self.name)

    def to_json(self):
        return dumps(self.__store__, default=self.__encoder__)
