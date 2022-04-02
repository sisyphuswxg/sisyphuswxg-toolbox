
```python
import pymysql
import os


class connmysql(object):
    
    #对象第一次为None
    obj = None   
    
    def __new__(cls, *args, **kwargs): 
        if cls.obj is None:     
            cls.obj = super().__new__(cls)  
        return cls.obj  
    
    def __init__(self, user, password, database, host="localhost", port=3306):
        try:
            self.db=pymysql.connect(host=host, 
                                    port=port, 
                                    user=user, 
                                    password=password, 
                                    database=database, 
                                    charset="utf8")
        except Ellipsis as e:
            print(e)
            # 如果第一步的链接失败，下面的所有代码都不用走，直接退出
            os._exit(0)   

        self.cs = self.db.cursor()   #2.得到一个游标对象

    def query(self,sql):
        """
        负责查询功能
        """
        try:
            self.cs.execute(sql)
        except Exception as e:
            print(e)
            return
        ret = self.cs.fetchall()
        return ret   
    
    def update(self, sql):
        """
        负责更新功能
        """
        try:
            self.cs.execute(sql)
        except Exception as e:
            print(e)
            return
        # 需要提交：如果不进行提交，所有的改变(insert, delete, update)不会生效
        self.db.commit()
        print("更新成功！")


    def __del__(self):
        self.cs.close()  
        self.db.close()

        
a = connmysql(user="root",password="mysql",database="jingdong")
c = a.query(sql=input("输入sql语句："))
print(c)
a.update(sql=input('更新内容：'))
```