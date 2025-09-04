planetas = [] 
def adicionar_planeta():
    nome = input("digite o nome do planeta:" )
    tamanho = float(input("digite o tamanho do planeta (em km):"))
    distancia = float(input("digite a distancia do sol (em milhões de km):"))

    planeta = {
        "nome": nome,
        "tamanho": tamanho,
        "distancia": distancia 
        }  
    planetas.append(planeta)
    print(f"\n planeta '{nome}) registrado com sucesso!")
   
    adicionar_planeta()
    print(planetas)