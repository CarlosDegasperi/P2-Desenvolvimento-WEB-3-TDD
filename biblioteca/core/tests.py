from django.test import TestCase
from django.shortcuts import resolve_url as r
from http import HTTPStatus
from .models import LivroModel
from .forms import LivroForm


class IndexGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class IndexPostTest(TestCase):
    def setUp(self):
        self.resp = self.client.post(r('core:index'))
        self.resp2 = self.client.post(r('core:index'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.FOUND)
        self.assertEqual(self.resp2.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp2, 'index.html')


class CadastroGetTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:cadastro'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 9),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostOk(TestCase):
    def setUp(self):
        data = {'titulo': 'Contos de Machado de Assis',
                'editora': 'Editora Brasil',
                'autor': 'Machado de Assis',
                'isbn': '1111111111111',
                'paginas': '123',
                'ano': '2023'}
        self.resp = self.client.post(r('core:cadastro'), data, follow=True)
        self.resp2 = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'index.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
        self.assertEqual(self.resp2.status_code , HTTPStatus.FOUND)

    def test_dados_persistidos(self):
        self.assertTrue(LivroModel.objects.exists())

    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 2),
            ('<br>', 3),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class CadastroPostFail(TestCase):
    def setUp(self):
        data = {'titulo': 'Livro sem editora',}
        self.resp = self.client.post(r('core:cadastro'), data)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'cadastro.html')

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)

    def test_dados_persistidos(self):
        self.assertFalse(LivroModel.objects.exists())


class ListarGet_withoutBook_Test(TestCase):
    def setUp(self):
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_withoutBook_Test(TestCase):
    def setUp(self):
        data = {}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Nenhum livro cadastrado', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarGet_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',)
        self.livro.save()
        self.resp = self.client.get(r('core:listar'), follow=True)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'listar.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 4),
            ('Contos de Machado de Assis', 1),
            ('<br>', 2),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class ListarPost_OneBook_Test(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',)
        self.livro.save()
        data = {'livro_id': self.livro.pk}
        self.resp = self.client.post(r('core:listar'), data)

    def test_status_code(self):
        self.assertEqual(self.resp.status_code , HTTPStatus.OK)
    
    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'detalhes.html')
    
    def test_found_html(self):
        tags = (
            ('<html', 1),
            ('<body>', 1),
            ('Biblioteca', 2),
            ('<input', 1),
            ('Contos de Machado de Assis', 1),
            ('<br>',5),
            ('</body>', 1),
            ('</html>', 1),
        )
        for text, count in tags:
            with self.subTest():
                self.assertContains(self.resp, text, count)


class LivroModelModelTest(TestCase):
    def setUp(self):
        self.livro = LivroModel(
            titulo='Contos de Machado de Assis',
            editora='editora Brasil',
            autor='Machado de Assis',
            isbn='1111111111111',
            paginas='123',
            ano='2023')
        self.livro.save()

    def test_created(self):
        self.assertTrue(LivroModel.objects.exists())


class LivroFormTest(TestCase):
    def test_fields_in_form(self):
        form = LivroForm()
        expected = ['titulo', 'editora', 'autor', 'isbn', 'paginas', 'ano']
        self.assertSequenceEqual(expected, list(form.fields))
    
    def test_form_all_OK(self):
        dados = dict(titulo='Contos do Machado de Assis', editora='Editora Brasil',
                     autor='Machado de Assis', isbn='1111111111111', paginas='123', ano='2023')
        form = LivroForm(dados)
        errors = form.errors
        self.assertEqual({}, errors)
        
    def test_form_without_data_1(self):
        dados = dict(editora='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Informe a EDITORA do livro.'
        self.assertEqual([msg], errors_list)

    def test_form_without_data_2(self):
        dados = dict(titulo='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Informe o TÍTULO do livro.'
        self.assertEqual([msg], errors_list)
    
    def test_form_without_data_3(self):
        dados = dict(autor='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['autor']
        msg = 'Informe o AUTOR do livro.'
        self.assertEqual([msg], errors_list)
        
    def test_form_without_data_4(self):
        dados = dict(isbn='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['isbn']
        msg = 'Informe o ISBN do livro.'
        self.assertEqual([msg], errors_list)        
        
    def test_form_without_data_5(self):
        dados = dict(paginas='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['paginas']
        msg = 'Informe QT PÁGINAS do livro.'
        self.assertEqual([msg], errors_list)        
    
    def test_form_without_data_6(self):
        dados = dict(ano='')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['ano']
        msg = 'Informe o ANO do livro.'
        self.assertEqual([msg], errors_list)    
    
    def test_form_less_than_03_character_1(self):
        dados = dict(titulo='Co')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['titulo']
        msg = 'Deve ter pelo menos TRES caracteres'
        self.assertEqual([msg], errors_list)
            
    def test_form_less_than_03_character_2(self):
        dados = dict(editora='12')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['editora']
        msg = 'Deve ter pelo menos TRES caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_10_character_1(self):
        dados = dict(autor='Machado')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['autor']
        msg = 'Autor deve ter pelo menos DEZ caracteres'
        self.assertEqual([msg], errors_list)

    def test_form_less_than_13_character_1(self):
        dados = dict(isbn='1234567890')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['isbn']
        msg = 'ISBN deve ter TREZE caracteres'
        self.assertEqual([msg], errors_list)
        
    def test_form_less_than_03_character_3(self):
        dados = dict(paginas='A')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['paginas']
        msg = 'PÁGINAS deve ter UM a TRES caracteres e NUMÉRICOS'
        self.assertEqual([msg], errors_list)        
        
    def test_form_less_than_04_character_1(self):
        dados = dict(ano='123A')
        form = LivroForm(dados)
        errors = form.errors
        errors_list = errors['ano']
        msg = 'ANO deve ter QUATRO caracteres e NUMÉRICOS'
        self.assertEqual([msg], errors_list)        
        