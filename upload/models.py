from email.mime import image
from django.db import models
from django.core.files.base import ContentFile
# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=30)
    document = models.ImageField(upload_to= 'media/')
    alt = models.TextField('alt', max_length=2000, default = '', blank= False, null= False )
    width = models.PositiveIntegerField('Largura da imagem', default=0, editable=False)
    height = models.PositiveIntegerField('Altura da imagem', default=0, editable=False)

    def to_dict(self):
        media_dict = {
            'title': self.title,
            'document': self.document,
            'alt': self.alt,
            'width': self.width, # mudar para self.document.width
            'heigth': self.height # mudar para self.document.height
        }
