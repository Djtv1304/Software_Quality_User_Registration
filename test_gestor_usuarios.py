import unittest
from gestor_usuarios import GestorUsuarios

class TestGestorUsuarios(unittest.TestCase):
    def test_agregar_usuario(self):
        gestor = GestorUsuarios()
        gestor.agregar_usuario("Ana", "ana@mail.com")
        self.assertIn("Ana", gestor.usuarios)
        self.assertEqual(gestor.usuarios["Ana"], "ana@mail.com")

    def test_correo_valido(self):
        gestor = GestorUsuarios()
        self.assertTrue(gestor.es_correo_valido("correo@dominio.com"))
        self.assertFalse(gestor.es_correo_valido("correo.com"))
        self.assertFalse(gestor.es_correo_valido("correo@com"))

    def test_actualizar_correo(self):
        gestor = GestorUsuarios()
        gestor.agregar_usuario("Luis", "luis@mail.com")
        gestor.actualizar_correo("Luis", "nuevo@mail.com")
        self.assertEqual(gestor.usuarios["Luis"], "nuevo@mail.com")

    def test_eliminar_usuario(self):
        gestor = GestorUsuarios()
        gestor.agregar_usuario("Sofía", "sofia@mail.com")
        gestor.eliminar_usuario("Sofía")
        self.assertNotIn("Sofía", gestor.usuarios)


