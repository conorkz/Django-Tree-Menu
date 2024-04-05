from django.db import models
from django.urls import reverse

class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    url = models.CharField(max_length=255, blank=True)
    url_name = models.CharField(max_length=50, blank=True)
    menu_name = models.CharField(max_length=50)

    def get_absolute_url(self):
        if self.url_name:
            return reverse(self.url_name)
        else:
            return self.url