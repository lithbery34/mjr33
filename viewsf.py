from django.shortcuts import render
from .models import info
import pyautogui
import time
from selenium import webdriver
def index(request):
    #HttpResponse('Hello world')
    b=request.GET.get('pro')
    inf=info()
    inf.name='iphone'
    inf.price=56000
    driver=webdriver.Firefox()
    # a=input('Enter elemnt')
    driver.get('https:flipkart.com/search?q='+'red')
    #pyautogui.click(3641, 286)
    #time.sleep(2)
    #pyautogui.typewrite(a)
    return render(request, "index2.html",{'inf':inf})
#def cmp(request):
    #infor=request.POST.post('pro')
    #driver=webdriver.Firefox()
    #a=input('Enter elemnt')
    #driver.get('https:flipkart.com/search?q='+a)
    ##info=driver.find_element_by_class_name('_1HmYoV _35HD7C')
    #driver.get('https:amazon.in/s?k='+a)
    #infzon=driver.find_element_by_class_name('s-main-slot s-result-list s-search-results sg-row')
    #driver.get('https:ebay.in/s?k=' + a)
    #infzon = driver.find_element_by_class_name('_4FmiYoP _sg-row')
    #info='bcd'
    #print(info)
    #print(infzon.text)
    return infor
