

```python
def connection_pool(n):
    # 限制连接池实例数量
    assert n < 20  
    
    def singleton(cls):
        # 创建一个列表用来保存类的实例对象
        _instance_list = list()
        def _singleton(*args, **kwargs):
            # 先判断这个实例列表有没有实例，即是不是类第一次init
            while len(_instance_list) < n:
                _instance_list.append(cls(*args, **kwargs))
            # 循环返回实例
            _instance_list.insert(0, _instance_list[-1])
            return _instance_list.pop()
        return _singleton
    return singleton
```


```python
import pymongo


MONGODB_URL = ""
MONGODB_DATABASE = ""


# 将三个连接实例加入连接池中
@connection_pool(3)  
class MongodbModule(object):
    def __init__(self,url = MONGODB_URL,db = MONGODB_DATABASE):
        self.myclient = pymongo.MongoClient(url)
        self.mydb = self.myclient[db]

        
# 循环返回mongodb的实例
mongo = MongodbModule()
```