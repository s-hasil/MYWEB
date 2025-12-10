from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

from django.shortcuts import render, redirect
from .models import ContactMessage
from django.contrib import messages


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            message=message
        )
        return redirect('thank_you')  # or redirect to a thank you page

    return render(request, 'contact.html')

def thank_you(request):
    return render(request, 'thank-you.html')  # simple success page

def pricing(request):
    return render(request, 'pricing.html')



from django.shortcuts import render, redirect
from .models import BugReport

def bug_reports(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        bug_type = request.POST.get("bug_type")
        page_url = request.POST.get("page_url")
        description = request.POST.get("description")

        BugReport.objects.create(
            name=name,
            email=email,
            bug_type=bug_type,
            page_url=page_url,
            description=description
        )
        return redirect("thank_you")  # put your success page name

    return render(request, "bug_reports.html")