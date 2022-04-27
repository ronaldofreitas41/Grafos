class Grafo:
  def __init__(self, num_vert = 0, lista_adj = None, mat_adj = None):
    # construtor deum  grafo
    self.num_vert = num_vert
    
    if lista_adj == None:
      # Verifica se a lista de adjacencias do grafo está nula
      self.lista_adj = [[]for i in range(num_vert)]
    else:
      #Caso ela nao esteja nula a adicionamos em sua devida posição 
      self.list_adj = lista_adj
    
    if mat_adj == None:
      #Caso a matriz de adjacencia seja nula a criamos como vazia
      self.mat_adj = [[0 for i in range(num_vert)] for j in range(num_vert)] 
    else:
      #Caso ela nao esteja nula                                          
      self.mat_adj = mat_adj

  def add_aresta(self, u, v, w = 1):
    # Adiciona aresta de u a v com peso w de valor defaut 1
    self.num_arestas += 1
    if u < self.num_vert and v < self.num_vert:
      self.lista_adj[u].append((v, w))
      self.mat_adj[u][v] = w
    else:
      print("Aresta invalida!")

  def remove_aresta(self, u, v):
    # Remove aresta de u a v, se houver
    if u < self.num_vert and v < self.num_vert:
      if self.mat_adj[u][v] != 0:
        self.num_arestas += 1
        self.mat_adj[u][v] = 0
        for (v2, w2) in self.lista_adj[u]:
          if v2 == v:
            self.lista_adj[u].remove((v2, w2))
            break
      else:
        print("Aresta inexistente!")
    else:
      print("Aresta invalida!")

  def grau(self, u):
    # Retorna o grau do vertice u
    return len(self.lista_adj[u])

  def adjacente(self, u, v):
    # Determina se v é adjacente a u
    
    if self.mat_adj[u][v] != 0:
      return True
    else:
      return False

  def adjacentes(self, u):
    # Retorna a lista dos vertices adjacentes a u
    return self.lista_adj[u]

  def ler_arquivo(self, nome_arq):
    # Le arquivo de grafo no formato dimacs
    try:
      arq = open(nome_arq)
      #Leitura do cabecalho
      str = arq.readline()
      str = str.split(" ")
      self.num_vert = int(str[0])
      self.num_arestas = int(str[1])
      #Inicializacao das estruturas de dados
      self.lista_adj = [[] for i in range(self.num_vert)]
      self.mat_adj = [[0 for j in range(self.num_vert)] for i in range(self.num_vert)] 
      #Le cada aresta do arquivo
      for i in range(0,self.num_arestas):
        str = arq.readline()
        str = str.split(" ")
        u = int(str[0])
        v = int(str[1])
        w = int(str[2])
        self.add_aresta(u, v, w)
    except IOError:
      print("Nao foi possivel encontrar ou ler o arquivo!")
      
  def complementar(self):
    
    gc = [[0 for i in range(self.num_vert)] for j in range(self.num_vert)] 
    
    for i in range(len(self.mat_adj)):
      for j in range(len(self.mat_adj[i])):
        if(self.mat_adj[i][j]!= 0 or i==j):
          gc[i][j] = 0
        else:
          gc[i][j] = 1
    return gc

  def subgrafo(self,g2):
    if(self.num_arestas > g2.num_arestas):
      return False
      
    for i in range(len(self.lista_adj)):
        if(self.lista_adj[i] == 0 and g2.lista_adj[i] == 1):
          return False
    return True
    
  def buscaLargura(self,s):
  
    desc = [ 0 for i in range(len(self.lista_adj)) ]
    Q = [s]
    R = [s]
    desc[s] = 1
  
    while len(Q) != 0 :
      u = Q.pop(0)
      
      for v in self.lista_adj[u] :
        if desc [v[0]] == 0 :
  
          Q.append(v[0])
          R.append(v[0])
  
        desc [v[0]] = 1
      
    return R     

  def buscaProfundidade(self, s):
    desc = [0 for i in range ( len (self.lista_adj) ) ]
    S = [s]
    R = [s]
    desc [s] = 1
    while len (S) != 0 :
      u = S[-1]
      desempilhar = True
      
      for v in self.lista_adj[u]:
        
        if desc[v[0]] == 0 :
          desempilhar = False
          S.append(v[0])
          R.append (v[0])
          desc[v[0]] = 1
          break  
          
      if desempilhar :
          S.pop()
        
    return R


  def buscaProfundidadeRec(self, s, r ,desc ):
    r.append(s)
    desc[s] = 1
    for v in self.lista_adj[ s ] :
      if desc[v[0]] == 0 :
        self.buscaProfundidadeRec( v[0] , r, desc)
    return r

  def conexo(self,s,r,desc):
    r.append(s)
    desc[s] = 1
    for v in self.lista_adj[ s ] :
      if desc[v[0]] == 0 :
        self.buscaProfundidadeRec( v[0] , r, desc)
        
    for i in range(len(desc)):
      if i == 0:
        return False
    return True

  def ciclo(self,s):
    desc = [ 0 for i in range(len(self.lista_adj)) ]
    Q = [s]
    R = [s]
    desc[s] = 1
  
    while len(Q) != 0 :
      u = Q.pop(0)
      
      for v in self.lista_adj[u] :
        if desc[v[0]] == 1:
          return True
        
        if desc [v[0]] == 0 :
  
          Q.append(v[0])
          R.append(v[0])
  
        desc [v[0]] = 1
    return False      
    
    