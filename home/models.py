# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Service(models.Model):

    #__Service_FIELDS__
    hostname = models.CharField(max_length=255, null=True, blank=True)
    port = models.CharField(max_length=255, null=True, blank=True)

    #__Service_FIELDS__END

    class Meta:
        verbose_name        = _("Service")
        verbose_name_plural = _("Service")


class Users(models.Model):

    #__Users_FIELDS__
    password = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Users_FIELDS__END

    class Meta:
        verbose_name        = _("Users")
        verbose_name_plural = _("Users")


class Assets(models.Model):

    #__Assets_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    ip = models.CharField(max_length=255, null=True, blank=True)
    managed = models.BooleanField()

    #__Assets_FIELDS__END

    class Meta:
        verbose_name        = _("Assets")
        verbose_name_plural = _("Assets")



#__MODELS__END
