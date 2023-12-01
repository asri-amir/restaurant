from django.db import models
from django.utils.translation import gettext


class Food(models.Model):
    FOOD_TYPE = [
        ('breakfast', 'صبحانه'),
        ('drinks', 'نوشیدنی'),
        ('dinner', 'شام'),
        ('lunch', 'ناهار'),
    ]
    name = models.CharField(gettext('نام'), max_length=100)
    description = models.CharField(gettext("توضیحات"), max_length=50)
    rate = models.IntegerField(gettext('امتیاز'), default=0)
    price = models.IntegerField(gettext('قیمت'))
    time = models.IntegerField(gettext('زمان لازم'))
    pub_date = models.DateField(gettext('تاریخ انتشار'), auto_now=False, auto_now_add=True)
    photo = models.ImageField(gettext('عکس'), upload_to='foods/')
    type_food = models.CharField(gettext('نوع غذا'), max_length=10, choices=FOOD_TYPE, default='drinks')

    def __str__(self):
        return self.name




