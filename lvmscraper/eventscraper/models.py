from django.db    import models
from django.utils import timezone

class Event(models.Model):
    venue      = models.CharField(max_length=30)
    title      = models.CharField(max_length=30)
    date       = models.DateField()
    date_added = models.DateField(default=timezone.now)
    time       = models.CharField(max_length=30,null=True)
    URL        = models.CharField(max_length=80)

    def __str__(self):
        #Object name that is displayed in admin
        return self.title
        
    class Meta:
        permissions = (
            ("view_eventscraper", "Can see eventscraper content"),
            ("receive_emailupdates", "Will get email updates"),
        )