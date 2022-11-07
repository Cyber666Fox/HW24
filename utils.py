import re
from typing import Union, Optional, Iterable


def perform_query(cmd: Optional[str], val: Union[str, int], file: Iterable) -> list:
    if cmd == "filter":
        res = filter(lambda x: val in x, file)
        return list(res)

    if cmd == "map":
        return [x.split(" \"")[int(val)] for x in file]

    if cmd == "unique":
        return list(set(file))

    if cmd == "sort":
        if val == "asc":
            return sorted(file)
        elif val == "desc":
            return sorted(file, reverse=True)

    if cmd == "limit":
        return list(file)[0:int(val)]

    if cmd == "regex":
        reg = re.compile(r"%s" % val, re.I)
        return [x for x in file if reg.findall(x)]

    return []
