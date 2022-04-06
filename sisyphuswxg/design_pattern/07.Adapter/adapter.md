## 适配器模式


适配器模式(Adapter pattern)是一种结构型设计模式，帮助我们实现两个不兼容接口之间的兼容。

将某个类的接口转换为接口客户所需的类型。
将一个接口转换成客户希望的另一个接口，适配器模式使接口不兼容的那些类可以一起工作，其别名为包装器（Wrapper）


Demo1：
不同的国家，使用不同形状的电源插座。很多时候，它们的形状使得电子设备的插头不适合。那么，您如何将手机或笔记本电脑的充电器连接到这些电源插座？
-> 您将获得一个适配器，将其放入电源插座，然后将其插入适配器的另一端，适配器更改了插头的形状，以便可以使用电源插座。
-> 适配器不提供任何附加功能。它只是让您将插头连接到电源插座。

Demo2:
最新款的macbook pro，电脑的数据接口都变成了Type c接口,这导致了之前的所有的usb设备都不可用。
-> 这个时候就需要淘宝买一个能够将type c 转换成usb的器件，我们称之为适配器。

Demo3：
如果我们希望把一个老组件用于一个新系统中，或者把一个新组件用于一个老系统中，不对代码进行任何修改两者就能够通信的情况很少见。
但又并非总是能修改代码，或因为我们无法访问这些代码(例如，组件以外部库的方式提供)，或因为修改代码本身就不切实际。
在这些情况下，我们 可以编写一个额外的代码层，该代码层包含让两个接口之间能够通信需要进行的所有修改。这个代码层就叫适配器。


> **模式动机：**
> - 在软件开发中采用类似于电源适配器的设计和编码技巧被称为适配器模式。 
> - 通常情况下，客户端可以通过目标类的接口访问它所提供的服务。有时，现有的类可以满足客户类的功能需要，但是它所提供的接口不一定是客户类所期望的，这可能是因为现有类中方法名与目标类中定义的方法名不一致等原因所导致的。
> - 在这种情况下，现有的接口需要转化为客户类期望的接口，这样保证了对现有类的重用。如果不进行这样的转化，客户类就不能利用现有类所提供的功能，适配器模式可以完成这样的转化。
> - 在适配器模式中可以定义一个包装类，包装不兼容接口的对象，这个包装类指的就是适配器(Adapter)，它所包装的对象就是适配者(Adaptee)，即被适配的类。
> - 适配器提供客户类需要的接口，适配器的实现就是把客户类的请求转化为对适配者的相应接口的调用。也就是说：当客户类调用适配器的方法时，在适配器类的内部将调用适配者类的方法，而这个过程对客户类是透明的，客户类并不直接访问适配者类。因此，适配器可以使由于接口不兼容而不能交互的类可以一起工作。这就是适配器模式的模式动机。


三个角色：
- Target(目标抽象类)： 

目标抽象类定义客户所需的接口，可以是一个抽象类或接口，也可以是具体类。
  (在类适配器中，由于java、php语言不支持多重继承，所以它只能是接口。)

- Adapter(适配器类)

它可以调用另一个接口，作为一个转换器，对Adaptee和Target进行适配。它是适配器模式的核心。

- Adaptee(适配者类)

适配者即被适配的角色，它定义了一个已经存在的接口，这个接口需要适配，适配者类包好了客户希望的业务方法。




### 类适配器

使用Python的多重继承特性。
(考虑到Python的多重继承特性，谨慎使用...)

插座类的输出是三脚，而台灯需要的是两脚插座，现在需要一个Adapter来实现适配插座。

```python
# Adaptee: 适配者类 -  插座类，提供三角插座
class Socket:
    def trigle(self):
        print('trigger power supply')

# target: 目标抽象类，定义客户所需的接口
class TableLamp:
    def need_two(self):
        print('two power supply')


# adapter:适配器类，可以调用另外一个接口，对Adaptee和target进行适配（是适配器模式的核心）
class Adapter(TableLamp, Socket):
    def need_two(self):
        self.trigle()


# client
if __name__ == '__main__':
    lamp = Adapter()
    lamp.need_two()


# 运行结果：
trigger power supply
```


### 对象适配器

同样是上面的例子，使用对象适配器来实现。

```python
# Adaptee: 适配者类 -  插座类，提供三角插座
class Socket:
    def trigle(self):
        print('trigger power supply')


# target: 目标抽象类，定义客户所需的接口
class TableLamp:
    def need_two(self):
        print('two power supply')


# adapter:适配器类，可以调用另外一个接口，对Adaptee和target进行适配（是适配器模式的核心）
class Adapter(TableLamp):

    def __init__(self, socket):
        self.socket = socket

    def need_two(self):
        self.socket.trigle()


# client
if __name__ == '__main__':
    s = Socket()
    lamp = Adapter(s)
    lamp.need_two()

    
# 运行结果：
trigger power supply
```


### 适配器类

核心思想：创建一个适配器类，通过`__dict__`将需要转化的类的方法注册到适配器，复写`__getattr__`使其在适配器函数查无方法的时候，执行`getattr`魔法方法。

```python
class A:

    def a(self):
        print("method a of Class A")


class B(object):

    def b(self):
        print("method b of Class B")


class C:
    def c(self):
        print("method c of Class C")


class Adapter:
    def __init__(self, classname, adapted_methods):
        self.classname = classname
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)


def main():
    objects = []
    obj_a = A()
    objects.append(Adapter(obj_a, dict(test=obj_a.a)))
    obj_b = B()
    objects.append(Adapter(obj_b, dict(test=obj_b.b)))
    obj_c = C()
    objects.append(Adapter(obj_c, dict(test=obj_c.c)))
    for obj in objects:
        obj.test()


if __name__ == "__main__":
    main()


# 运行结果：
method a of Class A
method b of Class B
method c of Class C
```

在调试上面demo的时候遇到了一个python报错：
```bash
Traceback (most recent call last):
  File "/Users/wangxg/code_wxg/ToolBox/sisyphuswxg-toolbox/demo2.py", line 39, in <module>
    test()
  File "/Users/wangxg/code_wxg/ToolBox/sisyphuswxg-toolbox/demo2.py", line 29, in test
    objects.append(Adapter(AA, dict(test=AA.a)))
  File "/Users/wangxg/code_wxg/ToolBox/sisyphuswxg-toolbox/demo2.py", line 20, in __init__
    self.__dict__.update = method
AttributeError: 'dict' object attribute 'update' is read-only

# 原因是：dict.update是一个方法，不是一个可以赋值的变量
# 解决办法：
self.__dict__.update = method 
# 修改为：
self.__dict__.update(method)
```