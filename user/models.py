from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify
# Create your models here.


class Article(models.Model):
    title = models.CharField(_("Judul"), max_length=100)
    description = models.TextField(_("Deskripsi"))
    image = models.ImageField(_("Gambar"), upload_to='article/')
    slug = models.SlugField(_("Slug"), editable=False)
    created_at = models.DateTimeField(
        _("buat"), auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(
        _("ubah"), auto_now=True, auto_now_add=False)

    def save(self):
        self.slug = slugify(self.title)
        return super().save()

    def __str__(self):
        return f'{self.id}. {self.title}'
