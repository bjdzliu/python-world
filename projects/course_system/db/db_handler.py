from conf import settings   # 导入配置文件
import os
import pickle
def save_data(obj):
    #拼接出用户目录路径
    print(settings.DB_PATH)
    user_dir_path=os.path.join(settings.DB_PATH,obj.__class__.__name__)
    if not os.path.exists(user_dir_path):
        os.mkdir(user_dir_path)
    #拼接出用户文件路径
    user_path=os.path.join(user_dir_path,obj.user)

    #将对象序列化后写入文件
    with open(user_path,'wb') as f:
        pickle.dump(obj,f)

#把cls名字传过来，然后根据名字查找文件夹
def select_data(cls,name):
    #拼接出用户目录路径
    user_dir_path=os.path.join(settings.DB_PATH,cls.__name__)
    user_path=os.path.join(user_dir_path,name)
    if os.path.exists(user_path):
        with open(user_path,'rb') as f:
            obj=pickle.load(f)
            return obj

