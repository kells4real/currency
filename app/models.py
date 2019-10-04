from django.db import models
from django.utils.text import slugify


class Currency(models.Model):
    name = models.CharField(max_length=50)
    rate = models.FloatField()
    slug = models.SlugField(max_length=60, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Currencies"

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Currency.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)



