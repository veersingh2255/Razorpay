from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import razorpay
from .models import coffee
#5267 3181 8797 5449

@ csrf_exempt
def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))*100
        client = razorpay.Client(auth =("rzp_test_dMK69HXiLxyGbN", "AemT8lDfhNgwX3Pm8tsyMZN6"))
        payment= client.order.create({'amount':amount, "currency":'INR', 'payment_capture': '1'})
        print(payment)
        Coffee = coffee(name = name, amount = amount, payment_id = payment['id'])
        Coffee.save()
        return render(request, "index.html", {'payment':payment})
    return render(request, "index.html")

@ csrf_exempt
def success(request):
    if request.method == 'POST':
       a = request.POST
       order_id = ''
       for key,r in a.items():
           if key == 'id':
                order_id = r
                break
       user = coffee.objects.filter(order_id).first()
       print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
       user.paid = True
       user.save()
       print(order_id)
    return render(request, "success.html")