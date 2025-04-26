# Herencia – Extensión y Reutilización de Código

# Al terminar esta sesión, los estudiantes serán capaces de:

# Explicar el concepto de herencia y sus beneficios en la POO.

# Crear subclases que hereden de una clase base, usando super().

# Extender y sobrescribir métodos de la clase padre en la subclase.

# Reconocer ventajas y precauciones al utilizar herencia simple y múltiple.

# Implementar ejemplos prácticos donde la herencia facilite la extensión de funcionalidades sin duplicar código.


# Herencia simple...
# la capacidad de una subclase que hereda atributos y metodos de una clase padre.

# class Subclase(ClasePadre):
    # #print(soy una subclase que hereda de una clase padre.)

# definimos que atributos o metodos vamos a llamar de la clase padre con la palabra resevada super(), que directamente llama al constructor para inicializar o complementar comportamientos.

# 3.2 Sobrescritura de Métodos
# Concepto: Una subclase puede redefinir (override) un método heredado para adaptar o ampliar su funcionalidad.

# Cómo hacerlo: Definiendo en la subclase un método con el mismo nombre. Se puede usar super().metodo() dentro de la nueva implementación.
