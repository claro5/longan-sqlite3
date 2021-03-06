from .flesh import Flesh


class FastFlesh(Flesh):
    """
    此类的目的是通过字段数组和值数组快速生成一个Flesh类对象
    """

    def __init__(self, fields=(), values=(), opt=None):
        dct = {}
        for i in range(len(fields)):
            dct[fields[i].name] = values[i] if opt is None else opt(values, i)
        Flesh.__init__(self, **dct)
