from django.contrib import admin
from .models import *
from django.forms import ModelForm

from PIL import Image

class AdminForm(ModelForm):
    MIN_RESOLUTION = (400, 400)

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.fields['image'].help_text = 'Загружайте изображения с минимальным разрешением {}x{}'.format(
            *self.MIN_RESOLUTION)

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        print(img.width, img.height)
        return image

admin.site.register(Customer)  # Регистрируем модели
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Book)
