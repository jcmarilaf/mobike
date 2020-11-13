from django.test import TestCase
from apps.Registro.models import Recorridos
from apps.Registro.forms import RecorridosForm
from django.test import Client

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """La página raíz se carga correctamente"""
        response = self.client.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)
    
    def test_requerimientos_url(self):
        c = Client()
        resp = c.get('http://localhost:8000/ingresar/')
        self.assertEqual(resp.status_code, 200)



