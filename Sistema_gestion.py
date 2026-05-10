import datetime
from abc import ABC, abstractmethod

# --- 1. SISTEMA DE LOGS (Manejo de Archivos) ---
def registrar_error(mensaje):
    """Guarda los errores en un archivo log.txt sin detener el programa."""
    with open("log_errores.txt", "a") as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{fecha}] ERROR: {mensaje}\n")

# --- 2. EXCEPCIONES PERSONALIZADAS ---
class ReservaInvalidaError(Exception):
    """Excepción para cuando un dato de la reserva no cumple los requisitos."""
    pass

# --- 3. CLASES ABSTRACTAS ---
class Persona(ABC):
    def __init__(self, id_persona, nombre):
        self._id = id_persona  # Encapsulamiento
        self._nombre = nombre

    @abstractmethod
    def mostrar_detalle(self):
        pass

class Servicio(ABC):
    def __init__(self, nombre_servicio, precio_base):
        self.nombre_servicio = nombre_servicio
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        pass

# --- 4. CLASES DERIVADAS (Implementación de Polimorfismo) ---
class Cliente(Persona):
    def __init__(self,id_persona, nombre):
        # Usamos super() para heredar los atributos de persona
        super().__init__(id_persona,nombre)
        
    def mostrar_detalle(self): 
        return f"Cliente: (self_nombre) (ID:(self_id))"

class ReservaDeSala(Servicio):
    def calcular_costo(self, horas):
        # Ejemplo de validación para lanzar excepción
        if horas <= 0:
            raise ReservaInvalidaError("La duración en horas debe ser mayor a cero.")
        return self.precio_base * horas

# --- 5. LÓGICA PRINCIPAL CON TRY/EXCEPT ---
def crear_reserva(cliente, servicio, cantidad):
    try:
        print(f"Procesando reserva para: {cliente.mostrar_detalle()}")
        total = servicio.calcular_costo(cantidad)
        print(f"Reserva exitosa: {servicio.nombre_servicio} | Total a pagar: ${total}")
    
    except ReservaInvalidaError as e:
        print(f"Error en la reserva: {e}")
        registrar_error(str(e))
    
    except Exception as e:
        print("Ocurrió un error inesperado. Revisa el log.")
        registrar_error(f"Inesperado: {str(e)}")
    
    finally:
        print("Fin de la operación.\n")

# --- PRUEBA INICIAL ---
if __name__ == "__main__":
    # Crear objetos
    cliente1 = Cliente("123", "David")
    sala_juntas = ReservaDeSala("Sala de Juntas VIP", 50000)

    # Simulación 1: Operación correcta
    crear_reserva(cliente1, sala_juntas, 3)

    # Simulación 2: Operación con error (para probar la excepción)
    crear_reserva(cliente1, sala_juntas, -1)