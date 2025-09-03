El código funciona, pero está muy repetitivo en la parte del carrito. En lugar de escribir un if por cada producto y luego otro bloque para imprimir cada elemento, 
pueden usar un bucle for que recorra la lista de productos seleccionados. Eso hará que el programa sea más corto, más limpio y más fácil
de mantener si mañana agregan más productos al catálogo.

Ejemplo de mejora con un for:

print("\n=== CARRITO ===")
total = 0

for producto in carrito:
    print(f"- {producto[0]}: ${producto[1]}")
    total += producto[1]

iva = 0.19 * total
precio_iva = total + iva

print(f"\nSubtotal: ${total}")
print(f"IVA (19%): ${iva}")
print(f"Total a pagar: ${precio_iva}")
