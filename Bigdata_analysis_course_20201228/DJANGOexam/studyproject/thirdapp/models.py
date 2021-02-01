from django.db import models

class DBTest(models.Model) :
    name = models.CharField(max_length=10)  # max_length 속성은 필수 (영/한 최대 10글자까지)
    age = models.IntegerField(null=True)    # 선택적으로 입력 가능

    def __str__(self):
        return self.name + ":" + str(self.age)
