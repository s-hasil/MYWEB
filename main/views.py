from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.html import strip_tags
from django.utils.http import url_has_allowed_host_and_scheme
from .models import ContactMessage, BugReport
from .forms import RegistrationForm, ProfileUpdateForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


# Basic pages
def index(request):
    return render( request, 'index.html' )


def about(request):
    return render( request, 'about.html' )


def service(request):
    return render( request, 'service.html' )


def contact(request):
    if request.method == 'POST':
        name = request.POST.get( 'name' )
        email = request.POST.get( 'email' )
        phone = request.POST.get( 'phone' )
        service = request.POST.get( 'service' )
        message = request.POST.get( 'message' )

        if not name or not email or not message:
            messages.error(request, 'Name, email, and message are required.')
            return render(request, 'contact.html')

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            service=service,
            message=message
        )
        messages.success(request, 'Thanks for reaching out! We will get back to you shortly.')
        return redirect( 'thank_you' )

    return render( request, 'contact.html' )


def thank_you(request):
    return render( request, 'thank-you.html' )


def pricing(request):
    return render( request, 'pricing.html' )


def bug_reports(request):
    if request.method == "POST":
        name = request.POST.get( "name" )
        email = request.POST.get( "email" )
        bug_type = request.POST.get( "bug_type" ) or "Not specified"
        page_url = request.POST.get( "page_url" )
        description = request.POST.get( "description" )
        screenshot = request.FILES.get( "screenshot" )

        if not name or not email or not description:
            messages.error(request, 'Name, email, and description are required.')
            return render(request, "bug_reports.html")

        BugReport.objects.create(
            name=name,
            email=email,
            bug_type=bug_type,
            page_url=page_url,
            description=description,
            screenshot=screenshot
        )
        messages.success(request, "Bug report submitted successfully.")
        return redirect( "thank_you" )

    return render( request, "bug_reports.html" )


# Authentication Views
def register_view(request):
    if request.user.is_authenticated:
        return redirect( 'index' )

    if request.method == 'POST':
        form = RegistrationForm( request.POST )
        if form.is_valid():
            user = form.save()
            messages.success( request, 'Registration successful! Please log in with your credentials.' )
            return redirect( 'login' )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error( request, '{}: {}'.format( field, error ) )
    else:
        form = RegistrationForm()

    return render( request, 'register.html', {'form': form} )


def login_view(request):
    if request.user.is_authenticated:
        return redirect( 'index' )

    if request.method == 'POST':
        email = request.POST.get( 'email' )
        password = request.POST.get( 'password' )

        try:
            user_obj = User.objects.get( email=email )
            user = authenticate( request, username=user_obj.username, password=password )
            if user is not None:
                login( request, user )
                messages.success( request, 'Welcome back, {}!'.format( user.username ) )

                # Handle next parameter safely
                next_url = request.GET.get( 'next' ) or request.POST.get( 'next' )
                if next_url and url_has_allowed_host_and_scheme(
                        url=next_url,
                        allowed_hosts=settings.ALLOWED_HOSTS,
                        require_https=request.is_secure()
                ):
                    return redirect( next_url )
                return redirect( 'index' )
            else:
                messages.error( request, 'Invalid email or password.' )
        except User.DoesNotExist:
            messages.error( request, 'Invalid email or password.' )

    return render( request, 'login.html' )


@login_required
def logout_view(request):
    logout( request )
    messages.success( request, 'You have been logged out successfully.' )
    return redirect( 'login' )


@login_required
def profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm( request.POST, instance=request.user )
        if form.is_valid():
            form.save()
            messages.success( request, 'Your username has been updated successfully!' )
            return redirect( 'profile' )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error( request, '{}: {}'.format( field, error ) )
    else:
        form = ProfileUpdateForm( instance=request.user )

    return render( request, 'profile.html', {'form': form} )



from .forms import CustomPasswordResetForm

class CustomPasswordResetView(PasswordResetView):
    email_template_name = 'password_reset_email.html'
    subject_template_name = 'password_reset_subject.txt'
    template_name = 'password_reset.html'
    success_url = '/password_reset_done/'
    form_class = CustomPasswordResetForm

