## 多线程下的单例使用问题

在使用类方法、__new__方法、元类来实现单例时，在单线程下是安全的。但是如果遇到多个线程同时创建这个类的实例的时候就会出现问题。

多线程下存在同时创建多个实例的现象，属于线程安全问题。当加入多线程去创建实例对象的时候，如果执行速度够快还不会出现影响，当执行速度不够快的时候，
一个线程去创建实例然后拿到了_instance这个属性去判断，其他的线程也可能会拿到_instance这个属性，发现并没有实例存在。
此时，这两个线程就会同时创建一个实例，造成同时创建多个实例的现象，那么单例模式自然也就失效了。

如下demo：创建了多个不同的实例。
```python
import threading
import time


class Person(object):

    def __init__(self,name, age):
        self.name = name
        self.age = age
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = cls(*args, **kwargs)
        return cls._instance


def task(arg):
    p = Person.get_instance('张三',18)
    print(p)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=[i,])
        t.start()
        

# 运行结果：
<__main__.Person object at 0x7fd27925aeb0>
<__main__.Person object at 0x7fd27927d1c0>
<__main__.Person object at 0x7fd27927d490>
<__main__.Person object at 0x7fd27927d760>
<__main__.Person object at 0x7fd27927da30>
<__main__.Person object at 0x7fd27927dd00>
<__main__.Person object at 0x7fd2792842e0>
<__main__.Person object at 0x7fd27927dfd0>
<__main__.Person object at 0x7fd279284880>
<__main__.Person object at 0x7fd2792845b0>
```


=> 解决办法：加线程锁
在获取对象属性_instance的时候加锁，让每一个线程使用完后才释放它，接着下一个线程继续运行程序，就可以解决同时获取对象并创建不同的实例的问题。

```python
import threading
import time


class Person(object):

    _lock = threading.Lock()

    def __init__(self,name, age):
        self.name = name
        self.age = age
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        with cls._lock:
            if not hasattr(cls, '_instance'):
                cls._instance = cls(*args, **kwargs)
        return cls._instance


def task(arg):
    p = Person.get_instance('张三',18)
    print(p)


if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=[i,])
        t.start()


# 运行结果：
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
<__main__.Person object at 0x7fac05a98040>
```


------

Demo1: 使用`__new__()`方法实现单例（改进版）
```python
import threading
import time
 

class Person(object):
    
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        time.sleep(1)
        with cls._lock:
            if not hasattr(cls, '_instance'):
                cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self,name, age):
        self.name = name
        self.age = age
 
 
def task(arg):
    p = Person('张三',18)
    print(p)
 
 
if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=[i,])
        t.start()
```

Demo2: 使用元类方法实现单例（改进版）
```python
import threading
import time
 

class Singleton(type):
    
    _lock = threading.Lock()
    
    def __call__(cls, *args, **kwargs):
        time.sleep(1)
        with cls._lock:
            if not hasattr(cls, "_instance"):
                cls._instance = super().__call__(*args, **kwargs)
        return cls._instance
 
 
class Person(metaclass=Singleton):
    def __init__(self,name, age):
        self.name = name
        self.age = age
 
 
def task(arg):
    p = Person('张三',18)
    print(p)
 
 
if __name__ == '__main__':
    for i in range(10):
        t = threading.Thread(target=task, args=[i,])
        t.start()
```









[1]. https://blog.csdn.net/weixin_39947314/article/details/112332877
