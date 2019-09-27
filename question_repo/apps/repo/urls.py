from django.conf.urls import url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    # 题目列表
    # url(r'^questions/$', TemplateView.as_view(template_name="questions.html"), name="questions"),
    # 贡献题目
    # url(r'^question/$', views.test, name="question"),
    url(r'^question/$', views.Question.as_view(), name="question"),

    url(r'^questions/$', views.QuestionsList.as_view(), name="questions"),
    # 题目详情，捕获了一个参数
    # url(r'^question/id/$', TemplateView.as_view(template_name="question_detail.html"), name="question_detail"),
    url(r'^question/(?P<id>\d+)/$', views.QuestionDetail.as_view(),
        name="question_detail"),


]