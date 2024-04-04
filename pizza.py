from ingredientes import vegetales, masas, proteinas

class Pizza():

    tamano = "familiar"
    precio = 10000
    
    vegetales = ["tomate", "aceitunas", "champiñones"]
    proteinas = ["pollo", "vacuno", "carne vegetal"]
    masas = ["tradicional", "delgada"]
    @staticmethod
    def validar_elemento(solicitado, posibles):
        return solicitado.lower() in posibles
    
    def orden(self):
        self.proteinas = input(f"""Proteina que prefieres:
        1. Vacuno
        2. Pollo
        3. Carne Vegetal
        """)

        self.vegetales = []
        self.vegetales.append(input(f"""Primer vegetal que prefieres:
        1. Tomate
        2. Aceitunas
        3. Champiñones
        """))

        self.vegetales.append(input(f"""Segundo vegetal que prefieres:
        1. Tomate
        2. Aceitunas
        3. Champiñones
        """))

        #tipo de masa
        self.tipo_masas =input(f"""Tipo de masa que prefieres:
        1. Delgada
        2. Tradicional
        """)

        self.pizza_valida = self.validar_elemento(self.proteinas, proteinas) and self.validar_elemento(self.vegetales[0],vegetales) and self.validar_elemento(self.vegetales[1],vegetales) and self.validar_elemento(self.tipo_masas, masas)

        