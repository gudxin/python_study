from django.shortcuts import render
# 不用模板
# Create your views here.

import logging
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT,level=logging.INFO)

from django.http import JsonResponse,HttpRequest, HttpResponse, HttpResponseBadRequest
import json
import simplejson



def reg(request:HttpRequest):
    try:
        payload = json.loads(request.body.decode())
        pressure = payload['pressure']
        # 数据库中去看看有没有


        return HttpResponse("welcome to zigbee")
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()
