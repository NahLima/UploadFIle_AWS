from django.db import models

# Create your models here.
class Media(models.Model):
    title = models.CharField(max_length=30)
    document = models.ImageField(upload_to= 'media/')
    alt = models.TextField('alt', max_length=2000, default = '', blank= False, null= False )
    width = models.PositiveIntegerField('Largura da imagem', default=0, editable=False)
    height = models.PositiveIntegerField('Altura da imagem', default=0, editable=False)

    @property
    def size(self):
        return self.width, self.height

    @property
    def url(self):
        return str(self.document)

    def to_dict(self):
        media_dict = {
            'title': self.title,
            'document': self.url,
            'alt': self.alt,
            'size': self.size
        }
