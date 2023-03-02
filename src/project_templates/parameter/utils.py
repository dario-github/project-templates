import logging
import shutil
import ssl
from pathlib import Path
from typing import Dict


def dict_to_class(data, class_map: Dict[str, type], last_key: str):
    """将字典转换为类

    Args:
        data (_type_): 将被转换的数据
        class_map (Dict[str, type]): 类映射，从字典中获取键对应的类
        last_key (str): 上一个键值

    Returns:
        _type_: 转换完成的新类
    """
    # If the last_key doesn't exist in the class map, simply return the data unchanged
    if last_key not in class_map.keys():
        return data

    # If the data is an instance of a dictionary, then we call the class from class_map
    if isinstance(data, dict):
        return class_map.get(last_key, class_map[last_key])(
            **{k: dict_to_class(v, class_map, k) for k, v in data.items()}
        )

    # If the data is an instance of a list, then loop through it and call class map
    elif isinstance(data, list):
        return [dict_to_class(v, class_map, last_key) for v in data]

    # Otherwise return the data as it was
    else:
        return data


def load_config(config_file: str, class_map: Dict[str, type], last_key: str):
    """从配置文件加载参数类

    Args:
        config_file (str): 参数文件地址.

    Returns:
        ConfigParams: 包含所有用于request信息的参数类
    """
    from ruamel.yaml import YAML

    # 使用 yaml 1.2
    yaml = YAML()

    # # define custom tag handler
    # def join(loader, node):
    #     seq = loader.construct_sequence(node)
    #     return "".join([str(i) for i in seq])

    # # register the tag handler
    # yaml.constructor.add_constructor("!join", join)

    with open(config_file, "r", encoding="utf-8") as f:
        data = yaml.load(f)
    config = dict_to_class(data, class_map, last_key)
    return config


def download_webfile(url: str, target_dir: str):
    """下载 `url` 中的文件到 `target_dir` 目录下

    Args:
        url (str): 下载地址.
        target_dir (str): 下载目录.
    """
    import os
    import urllib.request

    # 下载 `url` 中的文件到 `target_dir` 目录下
    file_path = Path(target_dir) / os.path.basename(url)
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)  # 创建一个SSLContext对象，指定TLSv1.2协议
    with urllib.request.urlopen(
        url, context=context
    ) as response:  # 打开一个URL，传入SSLContext对象
        with open(file_path, "wb") as file:  # 打开一个文件对象，传入'wb'模式
            shutil.copyfileobj(response, file)  # 将URL的内容复制到文件对象
    logging.info(f"Downloaded {file_path}")
    # 在目标目录记录下载过的网址，避免重复下载
    with open(Path(target_dir) / ".DOWNLOAD_RECORDS", "a", encoding="utf-8") as f:
        f.write(url + "\n")


def unzip_webfile(url: str, target_dir: str):
    import io
    import urllib.request
    import zipfile

    with urllib.request.urlopen(url) as response:
        with io.BytesIO(response.read()) as zipfile_bytes:
            # 将 Zip 文件解压到指定目录
            with zipfile.ZipFile(zipfile_bytes) as my_zipfile:
                my_zipfile.extractall(target_dir)
    logging.info(f"Downloaded {url} to {target_dir}")
    # 在目标目录记录下载过的网址，避免重复下载
    with open(Path(target_dir) / ".DOWNLOAD_RECORDS", "a", encoding="utf-8") as f:
        f.write(url + "\n")
