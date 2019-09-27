from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import Answers, UserLog, QuestionsCollection, AnswersCollection
from django.core.signals import request_finished

@receiver(request_finished)
def all_log(sender,**kwargs):
    print(sender,kwargs)
    print("使用信号记日志")

@receiver(post_save,sender=UserLog)
def send_mail(sender,instance,**kwargs):
    print(sender,instance,kwargs)
    import time
    time.sleep(20)
    print("xxxxxx发邮件需要20sxxxxx")
