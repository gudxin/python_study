"""zigbee URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# from django.http import HttpResponse ,JsonResponse
#
#
# # 模板
# from django.shortcuts import render
# from django.template.loader import get_template
# # from django.template import loader, RequestContext
#
#
#
#
# def index(request):
#     print(request)
#     print(type(request))
#
#     # tpl = loader.get_template('index.html')
#     # context = RequestContext(request, {'content': 'www.xiaogu.com'})
#     # return HttpResponse(tpl.render(context))
#
#     # 与上面三行代码效果相同
#     return render(request, 'index.html', {'user': 'hello xiaogu'}) #html str
#     # return JsonResponse({'user':'hello xiaogu'}) #json str


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^index/$', index),
    # url(r'^$', index),
    url(r'^user/', include('user.urls'))
]
