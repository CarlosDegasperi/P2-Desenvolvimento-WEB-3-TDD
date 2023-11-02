from django.db import models

class LivroModel(models.Model):
    titulo  = models.CharField('Título ', max_length=200)
    editora = models.CharField('Editora', max_length=200)
    autor   = models.CharField('Autor  ', max_length=200)
    isbn    = models.CharField('ISBN   ', max_length=13)
    paginas = models.CharField('Páginas', max_length=3)
    ano     = models.CharField('Ano    ', max_length=4)
    
    def __str__(self):
        return self.titulo
    