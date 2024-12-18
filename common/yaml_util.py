import yaml
import os


#获取项目路径
def get_object_path():
    # 获取当前脚本文件所在的绝对路径
    script_path = os.path.abspath(__file__)
    print("【get_object_path()】方法返回：" + os.path.dirname(script_path).split('common')[0])
    # 返回该路径的父目录，即工程路径
    return os.path.dirname(script_path).split('common')[0]

#读取config.yml文件
def read_config_file(one_node,two_node):
    with open(get_object_path()+"\\config.yml",encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        return value[one_node][two_node]

#读取extract.yml文件
def read_extract_file(one_node):
    with open(get_object_path()+"\\extract.yml",encoding='utf-8') as f:
        value = yaml.load(stream=f, Loader=yaml.FullLoader)
        print("value is ",value)
        return value[one_node]

#写入extract.yml文件a
def write_extract_file(data):
    with open(get_object_path()+"\\extract.yml",encoding='utf-8',mode='a') as f:
        yaml.dump(data=data, stream=f,allow_unicode=True )

#清空extract.yml文件a
def clear_extract_file():
    with open(get_object_path()+"\\extract.yml",encoding='utf-8',mode='w') as f:
        f.truncate()

# if __name__ == '__main__':
#     print(read_config_file('base','base_url'))
#     print(get_object_path())
