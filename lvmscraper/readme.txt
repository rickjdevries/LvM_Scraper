Add/edit the following lines to settings.py when setting up the project:

INSTALLED_APPS:
    'mainpage.apps.MainpageConfig',
    'eventscraper.apps.EventscraperConfig',
    'django_crontab',
    
# Login
LOGIN_REDIRECT_URL =  'mainpage:index'
LOGIN_URL = 'login'

CRONJOBS = [
    ('0 19 * * *', 'eventscraper.scripts.scrape_events'),  #Every day at 19:00h

    ('0 20 * * 0', 'eventscraper.scripts.send_mailupdate') #Every sunday at 20:00h
]

TIME_ZONE = 'Europe/Amsterdam'

STATIC_URL = '/static/'
STATIC_ROOT = "/var/www/applicationportal/application_portal/static/"

LOGIN_REDIRECT_URL = '/'
        
#Email
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'USERNAME@gmail.com'
EMAIL_HOST_PASSWORD = 'PASSWORD'
EMAIL_PORT = 587
EMAIL_USE_TLS = True