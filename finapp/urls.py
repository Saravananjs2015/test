from django.conf.urls import url
from . import views
urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^catagory$', views.catagory, name='catagory'),
url(r'^finadv$',views.finadv,name='finadv'),
url(r'^register$',views.register,name='register'),
url(r'^investPro$',views.investPro,name='investPro'),
url(r'^investForm$',views.investForm,name='investForm'),
url(r'^asstMan$',views.asstMan,name='asstMan'),
url(r'^asstForm$',views.asstForm,name='asstForm'),
url(r'^acverify$',views.acverify,name='acverify'),
url(r'^check$',views.check,name='check'),
url(r'^help$',views.help,name='help'),
url(r'^profile$',views.profile,name='profile'),
url(r'^validate_user$',views.validate_user,name='validate_user'),
url(r'^editname$',views.editname,name='editname'),
url(r'^updatename$',views.updatename,name='updatename'),
url(r'^edituser$',views.edituser,name='edituser'),
url(r'^updateuser$',views.updateuser,name='updateuser'),
url(r'^editphone$',views.editphone,name='editphone'),
url(r'^updatephone$',views.updatephone,name='updatephone'),
url(r'^editmail$',views.editmail,name='editmail'),
url(r'^updatemail$',views.updatemail,name='updatemail'),
url(r'^checkmail$',views.check_send_mail,name='check_send_mail')
]
