from django import forms
from django.core.exceptions import ValidationError
from core.models import LivroModel


def validate_title(value):
    if len(value) < 3:
        raise ValidationError('Deve ter pelo menos TRES caracteres')

def validate_autor(value):
    if len(value) < 10:
        raise ValidationError('Autor deve ter pelo menos DEZ caracteres')
    
def validate_isbn(value):
    if len(value) < 13:
        raise ValidationError('ISBN deve ter TREZE caracteres')
    if not value.isdigit():
        raise ValidationError('ISBN deve ter TREZE caracteres e NUMÉRICOS') 
               
def validate_paginas(value):
    if len(value) < 1:
        raise ValidationError('PÁGINAS deve ter UM a TRES caracteres')
    if not value.isdigit():
        raise ValidationError('PÁGINAS deve ter UM a TRES caracteres e NUMÉRICOS')

def validate_ano(value):
    if len(value) < 4:
        raise ValidationError('ANO deve ter QUATRO caracteres')
    if not value.isdigit():
        raise ValidationError('ANO deve ter QUATRO caracteres e NUMÉRICOS')


class LivroForm(forms.ModelForm):

    class Meta:
        model = LivroModel
        fields = ['titulo', 'editora', 'autor', 'isbn', 'paginas', 'ano']
        error_messages = {
            'titulo': {
                'required': ("Informe o TÍTULO do livro."),
            },
            'editora': {
                'required': ("Informe a EDITORA do livro."),
            },
            'autor': {
                'required': ("Informe o AUTOR do livro."),
            },     
            'isbn': {
                'required': ("Informe o ISBN do livro."),
            },
            'paginas': {
                'required': ("Informe QT PÁGINAS do livro."),
            },
            'ano': {
                'required': ("Informe o ANO do livro."),
            }
        }

    def clean_titulo(self):
        titulo = self.cleaned_data['titulo']
        validate_title(titulo)
        return titulo

    def clean_editora(self):
        editora = self.cleaned_data['editora']
        validate_title(editora)
        return editora
    def clean_autor(self):
        autor = self.cleaned_data['autor']
        validate_autor(autor)
        return autor
    def clean_isbn(self):
        isbn = self.cleaned_data['isbn']
        validate_isbn(isbn)
        return isbn
    def clean_paginas(self):
        paginas = self.cleaned_data['paginas'] 
        validate_paginas(paginas)
        return paginas
    def clean_ano(self):
        ano = self.cleaned_data['ano'] 
        validate_ano(ano)
        return ano  

    def clean(self):
        self.cleaned_data = super().clean()
        return self.cleaned_data

