try:
    vlan = int(input("Introduzca el número de VLAN: "))

    if 1 <= vlan <= 1005:
        print("La VLAN", vlan, "corresponde al rango NORMAL.")
    elif 1006 <= vlan <= 4094:
        print("La VLAN", vlan, "corresponde al rango EXTENDIDO.")
    else:
        print("Número de VLAN fuera de rango válido.")
except ValueError:
    print("Error: Por favor ingrese un número entero válido.")