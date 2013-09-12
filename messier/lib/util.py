import datetime

from json import JSONEncoder
from math import ceil
from time import mktime


class MessierJSONEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return JSONEncoder.default(self, obj)


def paginated(objects, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    total = len(objects)
    return {
        "items": objects[start:end],
        "total": total,
        "pages": int(ceil(total / float(per_page))),
    }
