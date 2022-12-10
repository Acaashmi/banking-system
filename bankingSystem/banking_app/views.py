from django.shortcuts import render,redirect
from .models import customerdetail,transectiondetail
import math
import json
from django.contrib import messages
# Create your views here.
from django.http import HttpResponse

def index(request):
    
   
    return render(request,"bank/index.html")

def customer(request):
    details=customerdetail.objects.all()
    if request.method == "POST":
        email = request.POST.get('email')
        semail = request.POST.get('semail')
        amt = request.POST.get('amt')
        try:
            amt = int(amt)
        except:
            print("enter amount")
        for i in details:
            print(email)
            if i.email == email:
                j = i
                id = i.id
                break
        for i in details:
            print(i.email,i.avail_bal,semail)
            if i.email==semail and amt< i.avail_bal and amt>0 :
                avail_bal = i.avail_bal - amt
                avail_bal2 = j.avail_bal + amt
                try:
                    query1 = transectiondetail(name=i.name, email=i.email,
                                                deb_amt=amt ,cr_amt=0 , ac_bal=avail_bal)

                    query2 = customerdetail(id=i.id, avail_bal=avail_bal, email=i.email
                                                    , name=i.name)
                    query3 = transectiondetail(name=j.name, email=j.email,
                                                deb_amt=0 ,cr_amt=amt , ac_bal=avail_bal2)
                    query4 = customerdetail(id=id, avail_bal=avail_bal2, email=j.email
                                                    , name=j.name)
                    query2.save()
                    query1.save()
                    query4.save()
                    query3.save()
                    
                    messages.success(request,"Transaction Successful")


                    break
                except:
                    messages.error(request,"Transaction Failed")
                    print("transection failed")
                    break
            elif i.email==semail and amt> i.avail_bal and amt>0 :
                messages.error(request,"Transaction Failed!! Insufficient Funds")  
                break      
        else:
            messages.error(request,"Invalid Data")
            print("invalid data")
    return render(request,"bank/customers.html",{'details':details})

def transaction(request):
    trans = transectiondetail.objects.all()
    return render(request,'bank/transaction.html',{'trans':trans})

def about(request):
    return render(request,"bank/about.html")