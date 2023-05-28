from django.db import models
from django.utils.translation import gettext_lazy as _


class Magazine(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Nashr nomi'))
    created_at = models.DateTimeField(verbose_name=_('Yaratilgan vaqti'))
    file = models.FileField(upload_to='magazine/', verbose_name=_('Fayl'))
    hajmi = models.CharField(max_length=100, verbose_name=_('Hajmi'))
    downloads_count = models.IntegerField(default=0, verbose_name=_('Yuklanishlar soni'))

    class Meta:
        verbose_name = _('Gazeta nashri')
        verbose_name_plural = _('Gazeta nashrlari')
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.hajmi = f'{self.file.size / 1000000:.2f} MB'
        super().save(*args, **kwargs)
        