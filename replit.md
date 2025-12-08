# ProWebSec - Django Web Application

## Overview
ProWebSec is a Django-based web application for a web security and development business. The application provides information about web development and security services, with pages for home, about, services, contact, pricing, and bug reports.

**Current State**: Successfully configured for Replit environment and ready for use.

## Recent Changes (December 8, 2025)
- **Initial Setup**: Configured project for Replit environment
- **Django Settings**: Updated for Replit proxy support with CSRF trusted origins
- **Static Files**: Configured WhiteNoise for static file serving and fixed CSS directory naming (uppercase to lowercase)
- **Workflow**: Set up Django development server on port 5000
- **Deployment**: Configured autoscale deployment with Gunicorn
- **Dependencies**: Installed Python 3.10 with Django 4.2, gunicorn, and whitenoise

## Project Architecture

### Technology Stack
- **Framework**: Django 4.2
- **Python**: 3.10
- **Database**: SQLite (development)
- **Static Files**: WhiteNoise middleware
- **Web Server**: 
  - Development: Django's built-in server (port 5000)
  - Production: Gunicorn

### Directory Structure
```
MYWEB/                 # Main Django project
├── settings.py        # Django settings (configured for Replit)
├── urls.py           # URL routing
├── wsgi.py           # WSGI application
main/                 # Main app
├── models.py         # ContactMessage model
├── views.py          # View functions
├── migrations/       # Database migrations
templates/            # HTML templates
├── index.html        # Homepage
├── about.html        # About page
├── service.html      # Services page
├── contact.html      # Contact form page
├── pricing.html      # Pricing page
├── bug_reports.html  # Bug reports page
├── thank-you.html    # Thank you page
static/               # Static files
├── css/             # Stylesheets
│   └── style.css
└── script.js        # JavaScript
```

### Key Features
1. **Contact Form**: Saves contact submissions to database via ContactMessage model
2. **Responsive Design**: Uses external CSS and Font Awesome icons
3. **Static File Management**: Configured with WhiteNoise for efficient serving
4. **Admin Interface**: Django admin available at /admin/

### Database Schema
- **ContactMessage Model**:
  - name (CharField)
  - email (EmailField)
  - phone (CharField, optional)
  - service (CharField, optional)
  - message (TextField)
  - date_submitted (DateTimeField, auto)

## Development

### Running Locally
The Django development server is configured to run automatically on `0.0.0.0:5000`. The workflow "Django Web Server" handles this.

### Database
The project uses SQLite for development. All migrations are already applied.

### Static Files
Static files are managed by WhiteNoise:
- Development: Files served from `static/` directory
- Production: Files collected to `staticfiles/` directory

To recollect static files:
```bash
python manage.py collectstatic --noinput
```

## Deployment
The project is configured for autoscale deployment using Gunicorn:
- **Build command**: Collects static files
- **Run command**: Gunicorn on port 5000 with reuse-port option
- **Target**: Autoscale (suitable for stateless web applications)

## Configuration Notes

### Replit-Specific Settings
- `ALLOWED_HOSTS = ['*']` - Accepts all hosts
- `CSRF_TRUSTED_ORIGINS` - Configured for Replit domains (*.replit.dev, *.repl.co, *.replit.app)
- `SECURE_PROXY_SSL_HEADER` - Configured to honor Replit's HTTPS proxy headers for correct CSRF behavior
- `X_FRAME_OPTIONS = 'ALLOWALL'` - Allows iframe embedding for Replit preview
- WhiteNoise middleware for static file serving
- Port 5000 for both development and production

### Security Considerations for Production
Before deploying to production, configure these settings via environment variables:
- `SECRET_KEY` - Currently hardcoded; should use environment variable
- `DEBUG` - Should be set to False in production
- `ALLOWED_HOSTS` - Should be restricted to specific domains
- Consider using PostgreSQL for production instead of SQLite
- Ensure SECURE_PROXY_SSL_HEADER is set to handle HTTPS correctly through Replit's proxy

## URLs
- `/` - Homepage
- `/about/` - About page
- `/service/` - Services page
- `/contact/` - Contact form
- `/pricing/` - Pricing page
- `/bug_reports/` - Bug reports page
- `/thank-you/` - Thank you page
- `/admin/` - Django admin interface
