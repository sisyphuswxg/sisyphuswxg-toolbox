## 工厂模式 

工厂模式，顾名思义就是我们可以通过一个指定的“工厂”获得需要的“产品”，在设计模式中主要用于抽象对象的创建过程，让用户可以指定自己想要的对象而不必关心对象的实例化过程。
这样做的好处是用户只需通过固定的接口而不是直接去调用类的实例化方法来获得一个对象的实例，隐藏了实例创建过程的复杂度，解耦了生产实例和使用实例的代码，降低了维护的复杂性。

分：简单工厂和工厂方法。


### 简单工厂

例子：生产Mercedes和BMW的汽车，如果没有“工厂”来生产它们，我们就要在代码中自己进行实例化，如下：
```python
class Mercedes(object):
    """梅赛德斯
    """
    def __repr__(self):
        return "Mercedes-Benz"

    
class BMW(object):
    """宝马
    """
    def __repr__(self):
        return "BMW"


# 实例化：
mercedes = Mercedes()
bmw = BMW()
```

考虑到现实中，可能会有很多汽车产品，而且每个产品的构造参数还不一样，因此在创建实例时会显得麻烦。
此时，可以构造一个"简单工厂"来把所有汽车的实例化过程封装起来。
封装起来之后，我们就可以通过向固定的接口传入参数来获得想要的对象实例。
```python
class SimpleCarFactory(object):
    """简单工厂
    """
    @staticmethod
    def product_car(name):
        if name == 'mb':
            return Mercedes()
        elif name == 'bmw':
            return BMW()
```


### 工厂方法

上面的例子有一个缺陷：当新增一种产品如Audi时，除了新增一个Audi类，还需要修改SimpleCarFactory类内部的product_car()方法。
-> 违背了软件设计中的开闭原则，即在扩展新的类时，尽量不要修改原有代码。

更好的办法是：在简单工厂的基础上把SimpleCarFactory抽象成不同的工厂，每个工厂对应生成自己的产品，这就是工厂方法。
如下demo：每个工厂负责生产自己的产品，当新增Audi产品时，只需要新增两个类：Audi类和一个AudiFactory类。
```python
#coding=utf-8
import abc

class AbstractFactory(object):
    """抽象工厂
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def product_car(self):
        pass

class MercedesFactory(AbstractFactory):
    """梅赛德斯工厂
    """
    def product_car(self):
        return Mercedes()

class BMWFactory(AbstractFactory):
    """宝马工厂
    """
    def product_car(self):
        return BMW()
    
    
# 实例化：
c1 = MercedesFactory().product_car()
c2 = BMWFactory().product_car()
```

