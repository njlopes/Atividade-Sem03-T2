PI = 3.141592
raio = float(input("Digite o raio: "))
circunferencia = 2 * PI * raio
a_circulo = PI * raio ** 2
a_esfera = 4 * PI * raio ** 2
vol_esfera = 4 / 3 * PI * raio ** 3
print("Circunferência: %5.6f " % (circunferencia))
print("Área do círculo: %5.6f" % (a_circulo))
print("Área da esfera: %5.6f" % (a_esfera))
print("Volume da esfera: %5.6f" % (vol_esfera))


