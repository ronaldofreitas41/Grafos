import Grafo 

g1 = Grafo.Grafo()
g2 = Grafo.Grafo()

g1.ler_arquivo("grafo1.txt")
g2.ler_arquivo("grafo2.txt")

print("Vertices alcancaveis de G1 não recursivel",g1.buscaProfundidade(0))

R = []
desc1 = [0 for i in range ( len (g1.lista_adj) ) ]

print("Vertices alcancaveis de G1 recursivel",g1.buscaProfundidadeRec(0, R ,desc1))
print("Conexo",g1.conexo(0, R ,desc1))
print("Ciclo",g1.ciclo(0))
