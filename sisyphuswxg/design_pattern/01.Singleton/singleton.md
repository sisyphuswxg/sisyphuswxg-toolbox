## 单例模式 

单例是一种 设计模式，应用该模式的类只会生成一个实例。
单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例，如果实例不存在，会创建一个实例；如果已存在就会返回这个实例。

> 举个例子来说：比如我们在自动化测试框架中，会经常用到数据库操作。假设测试环境有多套，而数据库的连接信息也是不相同的，
> 那么我们在框架中会定义一个工具类（Manager）专门来管理数据库的连接info、环境切换等。然后这个类可能会被很多地方调用，
> 每次调用这个类都会创建一个实例，那么问题来了 ?现在我不想程序每次调用的时候都创建一个实例，我想统一管理。我只创建一个实例，
> 当其他地方需要的时候直接调用这个实例即可，这样一来便于管理和节省资源。在这种情况下，单例模式 就可以大展拳脚了。

单例 vs 全局变量：
全局变量不能保证全局只有一个类的实例，完全可以声明同一个类的多个实例。当然，如果你注意一点，那么用全局方法保证全局只有一个该类的实例还是可以做到的，
但你要注意，让自己不要在其他地方声明多一个实例。而单例可以轻松的做到这一点，并能保证全局只有一个该类的实例可被访问。
其次，相对来说，使用单例时，代码会显得优雅一些。


Python实现单例的集中方式：
- 模块导入模拟
- 装饰器（函数装饰器、类装饰器）
- 使用`__new__`关键字
- 使用metaclass



### 模块导入模拟

Python的模块就是天然的单例模式。，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件， 而不会再次执行模块代码。
因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。

```python
# a.py
class Person:

    
    def __init__(self, name):
        self.__name = name

    def __repr__(self):
         return self.__name

    
angst = Person("Angst")


# b.py
from xxx import angst

print(angst)
```



### 装饰器

#### 函数装饰器

如下demo，demo1和demo2的id值相同，说明他们指向了同一个对象。
代码中巧妙的一行：`_instance = {}` -> 使用了不可变的类地址作为键，其实例作为值。每次创建实例时，
先检查该类是否存在实例，存在的话直接返回该实例即可，否则新建一个实例并存放在字典中。
可以打印`_instance`的值，为：`dict_items([(<class '__main__.Demo'>, <__main__.Demo object at 0x7fdb4d069c40>)])`

```python
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner


@singleton
class Demo(object):
    def __init__(self):
        pass


demo1 = Demo()
demo2 = Demo()
print(id(demo1) == id(demo2))


# 运行结果：
True
```


#### 类装饰器

和函数装饰器原理一样，只是用类装饰器实现。

```python
class Singleton(object):

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Demo:
    def __init__(self):
        pass


demo1 = Demo()
demo2 = Demo()
print(id(demo1) == id(demo2))


# 运行结果：
True
```

因为是类装饰器，还可以如下使用：
```python
class Singleton(object):

    def __init__(self, cls):
        self._cls = cls
        self._instance = {}

    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]


@Singleton
class Demo:
    def __init__(self):
        pass


demo1 = Demo()
demo2 = Demo()
print(id(demo1) == id(demo2))
```


### 使用`__new__`关键字

使用`__new__`方法在创建实例时进行干预，达到实现单例模式的目的。
如下demo，使用`_instance = None`来存放实例，如果`_instance`为None，则新建实例，否则直接返回`_instance`存放的实例。
```python
class Single(object):

    _instance = None

    def __new__(cls, *args, **kw):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kw)
        return cls._instance

    def __init__(self):
        pass


single1 = Single()
single2 = Single()
print(id(single1) == id(single2))
```
or:
```python
class Singleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance
 
    
class MyClass(Singleton):
    a = 1
```


### 使用metaclass

元类（metaclass)可以通过`__metaclass__`方法来创建类，在此过程中改变类的行为。

在实现单例之前，先了解使用`type()`创建类的方法：
```python
def func(self):
    print("do sth")


Klass = type("Klass", (), {"func": func})

k = Klass()
k.func()
```

如上，使用type创造了一个类出来，也是metaclass实现单例的基础。
如下demo：将metaclass指向Singleton类，让Singleton中的type来创建新的Demo实例。
```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Demo(metaclass=Singleton):
    pass


demo1 = Demo()
demo2 = Demo()
print(id(demo1) == id(demo2))
```





