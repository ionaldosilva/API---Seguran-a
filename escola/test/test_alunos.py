from rest_framework.test import APITestCase
from escola.models import Aluno
from django.urls import reverse
from rest_framework import status

class AlunoTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Alunos-list')
        aluno_1 = Aluno.objects.create(nome ='Aluno Teste1', rg = '123456789', cpf = '50803205082', data_nascimento = '2000-01-01')

    def test_requisicao_get_para_listar_aluno(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_requisicao_post_para_cadastrar_aluno(self):
        data={'nome':'Aluno Teste2','rg':'123456789','cpf':'50803205082', 'data_nascimento':'2001-01-02'}
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_put_para_atualizar_aluno(self):
        data={'nome':'Aluno Teste2 Atul','rg':'987654321','cpf':'50803205082', 'data_nascimento':'2001-01-02'}
        response = self.client.put('/alunos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

