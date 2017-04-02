from django.conf.urls import url
from .views import entry,cat,exitpage,dash,table
urlpatterns = [
    
       url(r'addexpense/$', entry,name='addEx_page'), 
       url(r'addcat/$', cat,name='addcat_page'), 
       url(r'cat/(?P<pk>.*)/$', table,name='table_page'),
       url(r'home/$', dash,name='home_page'),
       url(r'logout/$', exitpage,name='exit_page'), 
    ]