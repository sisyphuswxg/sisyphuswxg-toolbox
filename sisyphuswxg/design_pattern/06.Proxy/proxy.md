## 代理模式


代理模式完全解耦了调用方和被调用方之间的联系。

代理通常就是一个介于寻求方和提供方之间的中介系统。其核心思想就是客户端（寻求方）没有直接和提供方（真实对象）打交道， 而是通过代理对象来完成提供方提供的资源或操作。
代理其实就是封装实际服务对象的包装器或代理人。
代理可以为其包装的对象提供附加功能，而无需改变此对象的代码。
代理模式的主要目的是为其他对象提供一个代理者或占位符，从而控制对实际对象的访问。

(通俗，A和B想通话，必须通过C作为中间人牵线，此时A和B都只能给C说，C转换给对方)

应用场景：
- 远程（Remote）代理：为一个位于不同的地址空间的对象提供一个局域代表对象。这个不同的地址空间可以是在本机器中，也可是在另一台机器中。远程代理又叫做大使（Ambassador）。好处是系统可以将网络的细节隐藏起来，使得客户端不必考虑网络的存在。 
- 虚拟（Virtual）代理（图片延迟加载的例子）：根据需要创建一个资源消耗较大的对象，使得此对象只在需要时才会被真正创建。使用虚拟代理模式的好处就是代理对象可以在必要的时候才将被代理的对象加载；代理可以对加载的过程加以必要的优化。当一个模块的加载十分耗费资源的情况下，虚拟代理的好处就非常明显。 
- 保护代理（Protection Proxy ）控制对原始对象的访问。保护代理用于对象应该有不同 的访问权限的时候 
- 智能引用（Smart Reference）代理：当一个对象被引用时，提供一些额外的操作，比如将对此对象调用的次数记录下来等



Demo：模拟一个简单的远程代理例子。
(现在互联网圈都流行微服务架构，某公司将其项目拆出了商城服务A和用户服务B，A服务需要调用B服务的查询用户方法。现在来实现这个场景)

```python
from abc import abstractmethod


# 定义用户接口，A和B服务都引用此接口
class UserService:

    @abstractmethod
    def get_info(self, uid):
        pass


# 用户接口的实现，在B服务中
class UserServiceImpl(UserService):

    def get_info(self, uid):
        if uid == 1:
            return '张三'
        elif uid == 2:
            return '李四'
        elif uid == 3:
            return '王二'
        else:
            return None


# A服务不能直接调用B服务的方法，但是又想像使用本地方法一样调远程方法，所以增加了一层代理类
class UserServiceProxy(UserService):

    def __init__(self):
        # 这里应该是远程实现的，简单起见就直接new了
        self.userService = UserServiceImpl()
        print('我已经远程连接到了B服务')

    def get_info(self, uid):
        return self.userService.get_info(uid)


# A服务调用示例
if __name__ == '__main__':
    proxy = UserServiceProxy()
    print(proxy.get_info(2))
    print(proxy.get_info(5))


# 运行结果：
我已经远程连接到了B服务
李四
None
```