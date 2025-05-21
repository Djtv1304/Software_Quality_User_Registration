import re


class GestorUsuarios:
    def __init__(self):
        self.usuarios = {}

    def agregar_usuario(self, nombre, correo):
        self.usuarios[nombre] = correo

    def es_correo_valido(self, correo):
        return re.match(r"[^@]+@[^@]+\.[^@]+", correo) is not None

    def actualizar_correo(self, nombre, nuevo_correo):
        if nombre in self.usuarios and self.es_correo_valido(nuevo_correo):
            self.usuarios[nombre] = nuevo_correo

    def eliminar_usuario(self, nombre):
        if nombre in self.usuarios:
            del self.usuarios[nombre]






