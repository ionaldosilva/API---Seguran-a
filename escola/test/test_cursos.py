from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse
from rest_framework import status


class CursosTestCase(APITestCase):
    
    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(codigo_curso = 'CDTES1', descricao = 'Curso Teste 1', nivel = 'A')
        self.curso_2 = Curso.objects.create(codigo_curso = 'CDTES2', descricao = 'Curso teste 2', nivel = 'I')

    def test_requisicao_get_para_listar_cursos(self):
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
    
    def test_requisicao_post_para_cadastrar_cursos(self):
        data = {'codigo_curso':'CDTES3','descricao':'Curso teste 3','nivel':'A',}
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_delete_para_deletar_um_curso(self):
        response = self.client.delete('/cursos/1/',)
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_requisicao_put_para_atualizar_curso(self):
        data = {'codigo_curso':'CDTES1-AT','descricao':'Curso Teste Atualizado','nivel':'B'}
        response = self.client.put('/cursos/1/', data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
