from django.db import models

# Create your models here.
class Main(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to='image/',
        verbose_name="Фото"
    )
    page = models.IntegerField(
        default=1,
        verbose_name="Страница"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"