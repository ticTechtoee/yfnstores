from django.shortcuts import render
from .models import Products
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives

def index(request):
    prod = Products.objects.all()
    context = {'Products':prod}
    if request.method == "POST":
        custName = request.POST.get("name")
        custEmail = request.POST.get("email")
        custsubject = "Inquirey About " + request.POST.get("subject")
        custBody = request.POST.get("message")
        subject = custsubject
        email_body = "Email From Name : "+ custName + " Email Address : " + custEmail + " Inquiry About : "+ custBody
        
        from_email = settings.EMAIL_HOST_USER
        to_email = ("yfnstores@gmail.com", "")
        Emailmessage = EmailMultiAlternatives(
            subject=subject, body=email_body, from_email=from_email, to=to_email
        )
        Emailmessage.content_subtype = "html"
        Emailmessage.send()
        messages.success(request, "Message sent." )
    return render(request, 'home/index.html', context)

def prod_details(request,pk):
    prod = Products.objects.get(id = pk)
    return render(request, 'home/product-details.html',{'prod_detail':prod})
