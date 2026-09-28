from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse


class Vitrine(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vitrines')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('vitrine_publica', args=[self.slug])


class Produto(models.Model):
    CATEGORIES = [('beleza', 'Beleza'), ('casa', 'Casa'), ('moda', 'Moda'), ('tecnologia', 'Tecnologia'), ('outros', 'Outros')]
    vitrine = models.ForeignKey(Vitrine, on_delete=models.CASCADE, related_name='produtos')
    name = models.CharField(max_length=140)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORIES)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image_url = models.URLField(blank=True)
    partner_url = models.URLField(help_text='Link do parceiro, incluindo o seu código de afiliado quando houver.')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name
