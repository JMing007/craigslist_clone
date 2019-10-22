from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    # names the search itself instead of 'search object' 
    def __str__(self):
        return '{}'.format(self.search)

    # overrides the name in admin section. Auto adds 's' but Searches has an 'e'
    class Meta:
        verbose_name_plural = 'Searches'