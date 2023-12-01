from django.db import models
from django.utils.translation import gettext
from django.utils import timezone
from django.contrib.auth.models import User
# from ckeditor.fields import RichTextField


class Blog(models.Model):
    title = models.CharField(gettext('عنوان'), max_length=50)
    description = models.CharField(gettext('توضیحات'), max_length=100)
    content = models.TextField(gettext('متن'))
    created_at = models.DateTimeField(gettext('زمان انتشار'), default=timezone.now)
    author = models.ForeignKey(User, verbose_name=gettext('نویسنده'), on_delete=models.CASCADE)
    image = models.ImageField(gettext('تصویر'), upload_to='blogs/', blank=True, null=True)
    category = models.ForeignKey('Category', related_name='blog', verbose_name=gettext('دسته بندی'), on_delete=models.CASCADE, blank=True, null=True)
    tags = models.ManyToManyField('tag', verbose_name=gettext('تگ ها'), related_name='blogs', blank=True, null=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(gettext('عنوان'), max_length=50)
    slug = models.SlugField(gettext('نام لاتین'))
    published_at = models.DateTimeField(gettext('تاریخ انتشار'), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(gettext('عنوان'), max_length=50)
    slug = models.SlugField(gettext('نام لاتین'))
    published_at = models.DateTimeField(gettext('تاریخ انتشار'), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(gettext('تاریخ بروز رسانی'), auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title


class Comments(models.Model):
    blog = models.ForeignKey('Blog', verbose_name=gettext('مقاله'), related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(gettext('نام کاربر'), max_length=100)
    email = models.EmailField(gettext('ایمیل'), max_length=200)
    message = models.TextField(gettext('متن نظر'))
    date = models.DateField(gettext('تاریخ انتشار'), auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.email




