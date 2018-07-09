from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from views import calculator, student_manager


urlpatterns = [
   url(r'^sum/$', csrf_exempt(calculator.as_view()),
       name="Assignment-sum"),
   url(r'^list/$', csrf_exempt(student_manager.as_view()),
       name="Assignment-student_list"),
   url(r'^edit/(?P<id>\d+)/$', csrf_exempt(student_manager.as_view()),
       name="Assignment-student_delete"),
   url(r'^update/(?P<roll>\d+)/$', csrf_exempt(student_manager.as_view()),
       name="Assignment-student_edit")
]
