# Pequenos-proyectos-personales
Aquí iré subiendo ocasionalmente proyectos en base a ideas simples que se me vayan ocurriendo.

# 1) Calculadora de Física (Python)
Proyecto personal de primer semestre para practicar Python.

Permite calcular:
- MRU (distancia, velocidad, tiempo)
- Segunda Ley de Newton (F = m * a)
- Energía Cinética (Ec = 0.5 * m * v²)

## Cómo usar
Ejecuta "Calculadora_De_Física.py" y sigue el menú.

## Características
- Validación de entradas (try/except)
- Historial de cálculos
- Uso de match-case (Python 3.10+)



# 2) Calculadora de Fuerza Gravitacional (versión inicial)

Este programa calcula la **fuerza de atracción gravitacional** entre dos cuerpos del Sistema Solar (Sol, Mercurio, Venus, Tierra, Marte, Júpiter, Saturno, Urano) usando la **Ley de Gravitación Universal de Newton**.

## ¿Qué hace?

- Permite elegir dos cuerpos celestes de una lista numerada.
- Aplica la fórmula:  
   F = G · (m₁ · m₂) / d**2
- Usa la **distancia mínima posible** entre los cuerpos (cuando están alineados con el Sol) como aproximación.
- Muestra el resultado en Newtons con notación científica.

## ¿Cómo usarlo?

1. Ejecuta el programa en Python 3.10 o superior.
2. Elige dos objetos escribiendo su número:

1) Sol        2) Mercurio
3) Venus      4) Tierra
5) Marte      6) Júpiter
7) Saturno    8) Urano

3. El programa calculará la fuerza y te preguntará si quieres repetir o salir.

## Limitaciones actuales

- La distancia entre dos planetas **no es exacta**; se calcula como la diferencia de sus distancias al Sol (aproximación de distancia mínima, alineación perfecta).
- No se contemplan órbitas elípticas ni posiciones angulares reales.
- Es una herramienta **educativa**, no de precisión astronómica.
