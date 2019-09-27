import django.dispatch
# 自定义信号
mysignal = django.dispatch.Signal(providing_args=["arg1","arg2"])

#内置的信号是可以自动触发
#自定义的信号不能自动触发

from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver

# 当请求完成后，打印一个日志
@receiver(request_finished)
def all_log(sender,**kwargs):
    print(sender,kwargs)
    print("使用信号记日志")

# 当创建一条记录MailLog之后，会自动执行发送邮件

"""

@receiver(post_save,sender=MailLog)
def send_mail(sender,instance,**kwargs):
    pass

"""
