from django.db import models
from django.utils.text import slugify


class Game(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام بازی")
    description = models.TextField( verbose_name="توضیحات کوتاه")
    long_description = models.TextField(verbose_name="توضیحات کامل بازی",null=True , blank=True)
    image1 = models.ImageField(upload_to="images/", verbose_name="تصویر اول",null=True , blank=True)
    image2 = models.ImageField(upload_to="images/", verbose_name="تصویر دوم",null=True , blank=True)
    image3 = models.ImageField(upload_to="images/", verbose_name="تصویر سوم",null=True , blank=True)
    file_size = models.CharField(max_length=10 , verbose_name="حجم فایل" , null=True , blank=True)
    link_file = models.TextField(verbose_name= "لینک سایت" , null=True , blank=True)
    image = models.ImageField(upload_to="img/",null=True, verbose_name="تصویر")
    slug = models.SlugField(max_length=100, verbose_name="لینک")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(Game, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "بازی"
        verbose_name_plural = "بازی"


class GameDetails(models.Model):
    title = models.CharField(max_length=100, verbose_name="نام بازی")
    description = models.TextField(verbose_name="توضیحات کامل بازی")
    image1 = models.ImageField(upload_to="images/", verbose_name="تصویر اول")
    image2 = models.ImageField(upload_to="images/", verbose_name="تصویر دوم")
    image3 = models.ImageField(upload_to="images/", verbose_name="تصویر سوم")

    slug = models.SlugField(max_length=100, verbose_name="لینک")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.title))
        super(GameDetails, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "صفحه ی توضیحات"
        verbose_name_plural = "صفحه توضیحات بازی"

# Create your models here.
