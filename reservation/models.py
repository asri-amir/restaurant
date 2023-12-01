from django.db import models
from django.utils.translation import gettext


class Reservation(models.Model):
    name = models.CharField(gettext('نام و نام خانوادگی'), max_length=200)
    email = models.EmailField(gettext('ایمیل'), max_length=200)
    phone = models.CharField(gettext('تلفن'), max_length=20)
    number = models.IntegerField(gettext('تعداد'))
    date = models.DateField(gettext('تاربخ'), auto_now=False, auto_now_add=False)
    time = models.TimeField(gettext('ساعت'), auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.email

