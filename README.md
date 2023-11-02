# P2-Desenvolvimento-WEB-3-Prática TDD

Desafio técnico para os alunos da Fatec-Araras Disciplina "Desenvolvimento Web 3" e "Qualidade e Teste de Software"

Professor: Orlando Saraiva do Nascimento Jr

Desafio Sprint 2 - Devolvida com 97% de testes OK
Desenvolvido em Python 3.12 com Django
ATENÇÃO: Usar o Python 3.8 ou superior...

No ambiente Windows:

```console
git clone https://github.com/CarlosDegasperi/P2-Desenvolvimento-WEB-3-TDD.git
cd P2-Desenvolvimento-WEB-3-TDD
python -m venv venv
cd venv
cd scripts
activate.bat
cd ..
cd ..
pip install -r requirements.txt
cd biblioteca/
python manage.py migrate
python manage.py test
coverage run --source='.' manage.py test 
coverage html
python manage.py runserver

```
### Requisitos para a Sprint 2

Aqui começa seu desafio. Você deve implementar as seguintes melhorias:

#### Novos campos
O cliente deseja armazenar os novos campos referente a livros:

+ Autor
+ ISBN
+ Número de Páginas
+ Ano em que a obra foi escrita

#### Validação dos campos

O cliente deseja validar os campos com as seguintes regras:

+ Título:  Validar a string para cadastro com pelo menos 3 caracteres. Atualmente, espera-se ter pelo menos 10 caracteres.

+ Editora: Validar a string para cadastro com pelo menos 3 caracteres.
Atualmente, espera-se ter pelo menos 10 caracteres.

+ Autor: Validar a string para cadastro com pelo menos 10 caracteres.

+ ISBN: Validar a string para cadastro com exatos 13 caracteres e todos numéricos.

+ Número de Páginas: Validar a string para cadastro entre 1 e 3 caracteres e todos numéricos.

+ Ano: : Validar a string para cadastro com exatos 4 caracteres e todos numéricos. 

Além disso, na sprint 1, os campos Título e editora são obrigatórios. Nesta sprint, os novos campos serão obrigatórios também.

#### Ajustes nos testes

O código fonte passará por atualizações para acomodar estes novos requisitos. Com isso, você deve ajudar os testes existentes e, caso julgue pertinente, criar novos testes.

