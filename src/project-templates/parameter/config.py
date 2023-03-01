class CommanClass:
    """参数处理时的通用方法"""

    def __init__(self) -> None:
        pass


class ConfigParams(CommanClass):
    """处理参数文件的类"""

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
