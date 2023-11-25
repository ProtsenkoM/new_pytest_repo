import types
import allure


def auto_step(cls):
    for name, member in vars(cls).items():
        if not name.startswith('_'):
            if isinstance(member, (types.FunctionType, types.BuiltinFunctionType)):
                setattr(cls, name, allure.step(member))
            if isinstance(member, (classmethod, staticmethod)):
                inner_func = member.__func__
                method_type = type(member)
                decorated = method_type(allure.step(inner_func))
                setattr(cls, name, decorated)
    return cls


def singleton(_class):
    def _init(*args, **kwargs):
        if not hasattr(_class, 'instance'):
            setattr(_class, 'instance', _class(*args, **kwargs))
        return getattr(_class, 'instance')
    return _init