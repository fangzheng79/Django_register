from django.db import models

class User(models.Model):
    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=50)
    password = models.CharField(max_length=256)
    email = models.EmailField()
    sex = models.CharField(max_length=8,choices=gender,default='男')
    has_confirmed = models.BooleanField(default=False)
    c_time = models.DateTimeField(auto_now_add=True)   #auto_now_add为true则不能被修改

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户'
        verbose_name_plural = verbose_name



class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User',on_delete=models.CASCADE)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ":   " + self.code

    class Meta:

        ordering = ["-c_time"]
        verbose_name = "确认码"
        verbose_name_plural = "确认码"