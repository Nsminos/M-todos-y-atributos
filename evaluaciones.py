from pizza import Pizza



#a
print(f"Todas las pizzas tienen un tamaño {Pizza.tamano} y un precio {Pizza.precio}")
#b
print(Pizza.validar_elemento("salsa de tomate",["salsa de tomate", "salsa bbq"]))
#c
pizza_1 = Pizza()
print(pizza_1.tamano)
pizza_1.orden()
print(pizza_1.pizza_valida)

#d
print(f" Proteinas: {pizza_1.proteinas}, Vegetales: {pizza_1.vegetales}, Tipo de masa: {pizza_1.tipo_masas}. Es una pizza valida : {pizza_1.pizza_valida}")
#e
p = Pizza()
print(type(p))