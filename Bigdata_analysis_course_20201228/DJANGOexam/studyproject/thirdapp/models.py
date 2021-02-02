from django.db import models

class DBTest(models.Model) :
    name = models.CharField(max_length=10)  # max_length 속성은 필수 (영/한 최대 10글자까지)
    age = models.IntegerField(null=True)    # 선택적으로 입력 가능

    def __str__(self):
        return self.name + ":" + str(self.age)

class Emp(models.Model) :
    empno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=10)
    job = models.CharField(max_length=15)
    mgr = models.IntegerField()
    hiredate = models.DateField()
    sal = models.IntegerField()
    comm = models.IntegerField(null=True)
    deptno = models.IntegerField()

    def __str__(self):
        return str(self.empno)+","+self.ename +","+str(self.hiredate)+\
               ","+ str(self.sal) + ","+ str(self.deptno)