import random
from unidecode import unidecode
palavras = ['sagaz', 'âmago', 'termo', 'negro', 'êxito', 'mexer', 'nobre', 'senso', 'afeto', 'ética', 'algoz', 'plena', 'fazer', 'assim', 'tênue', 'mútua', 'sobre', 'aquém', 'seção', 'poder', 'vigor', 'sutil', 'porém', 'fosse', 'cerne', 'ideia', 'sanar', 'audaz', 'moral', 'inato', 'quiçá', 'desde', 'muito', 'justo', 'sonho', 'honra', 'torpe', 'razão', 'amigo', 'ícone', 'égide', 'etnia', 'fútil', 'anexo', 'dengo', 'tange', 'haver', 'lapso', 'então', 'expor', 'tempo', 'boçal', 'seara', 'hábil', 'saber', 'mútuo', 'casal', 'graça', 'óbice', 'xibiu', 'ávido', 'ardil', 'dizer', 'pesar', 'estar', 'dever', 'causa', 'tenaz', 'sendo', 'ainda', 'brado', 'pária', 'temor', 'crivo', 'coser', 'genro', 'comum', 'ápice', 'posse', 'prole', 'ânimo', 'assaz', 'ceder', 'corja', 'fugaz', 'pauta', 'detém', 'censo', 'culto', 'ânsia', 'atroz', 'digno', 'mundo', 'forte', 'mesmo', 'vulgo', 'vício', 'gleba', 'saúde', 'criar', 'cozer', 'todos', 'revés', 'jeito', 'valha', 'pudor', 'dogma', 'denso', 'neném', 'louco', 'atrás', 'regra', 'ordem', 'limbo', 'pedir', 'feliz', 'clava', 'homem', 'mercê', 'ajuda', 'usura', 'impor', 'banal', 'round', 'coisa', 'juízo', 'forma', 'legal', 'sábio', 'falso', 'certo', 'falar', 'prosa', 'servo', 'tenro', 'pífio', 'posso', 'presa', 'desse', 'cunho', 'herói', 'devir', 'viril', 'fácil', 'vendo', 'ontem', 'valor', 'visar', 'linda', 'manso', 'ébrio', 'sério', 'mágoa', 'meiga', 'puder', 'acaso', 'guisa', 'fluir', 'ímpio', 'reaça', 'afago', 'lugar', 'temer', 'platô', 'garbo', 'abrir', 'praxe', 'união', 'obter', 'gerar', 'burro', 'matiz', 'óbvio', 'cisma', 'afins', 'bruma', 'êxodo', 'vênia', 'pleno', 'crise', 'álibi', 'tédio', 'fluxo', 'ritmo', 'morte', 'senil', 'levar', 'havia', 'olhar', 'casta', 'enfim', 'tomar', 'visão', 'gênio', 'ouvir', 'prumo', 'parvo', 'brega', 'cabal', 'reles', 'parco', 'falta', 'vital', 'calma', 'bravo', 'outro', 'favor', 'tecer', 'pulha', 'terra', 'reter', 'vivaz', 'sábia', 'ameno', 'viver', 'tendo', 'único', 'força', 'laico', 'valia', 'passo', 'grato', 'nicho', 'achar', 'noção', 'carma', 'rever', 'papel', 'nossa', 'possa', 'ranço', 'pobre', 'rogar', 'noite', 'façam', 'dúbio', 'fardo', 'prime', 'ativo', 'farsa', 'coeso', 'fator', 'épico', 'anelo', 'claro', 'selar', 'óbito', 'líder', 'leigo', 'sesta', 'sinto', 'cesta', 'cisão', 'citar', 'ciúme', 'vazio', 'sonso', 'deter', 'atuar', 'ficar', 'velho', 'gente', 'tende', 'haste', 'adiar', 'humor', 'revel', 'ideal', 'fonte', 'sulco', 'ponto', 'árduo', 'labor', 'igual', 'marco', 'senão', 'remir', 'terno', 'exato', 'feixe', 'vemos', 'amplo', 'hiato', 'capaz', 'tanto', 'lavra', 'débil', 'cauda', 'relva', 'ciclo', 'inata', 'tenra', 'jovem', 'varão', 'ótica', 'chuva', 'gesto', 'ambos', 'raiva', 'pouco', 'caçar', 'coçar', 'toada', 'sonsa', 'velar', 'apoio', 'vácuo', 'série', 'imune', 'xeque', 'vimos', 'algum', 'farão', 'feito', 'horda', 'fusão', 'carro', 'advém', 'entre', 'leito', 'coesa', 'probo', 'minha', 'sente', 'sorte', 'cruel', 'trama', 'doido', 'anuir', 'frase', 'lazer', 'brisa', 'ímpar', 'verso', 'torço', 'chata', 'rigor', 'massa', 'botar', 'blasé', 'pegar', 'prece', 'maior', 'dorso', 'seita', 'moção', 'áurea', 'fauna', 'signo', 'furor', 'livro', 'preso', 'agora', 'plano', 'covil', 'liame', 'vetor', 'credo', 'comer', 'saiba', 'flora', 'casto', 'ocaso', 'senda', 'morar', 'praia', 'pecha', 'adeus', 'nunca', 'faina', 'dócil', 'aliás', 'peste', 'houve', 'árido', 'setor', 'ardor', 'ambas', 'mudar', 'manha', 'parte', 'peixe', 'rezar', 'antro', 'visse', 'risco', 'vírus', 'meses', 'salvo', 'vulto', 'junto', 'pajem', 'beata', 'saída', 'breve', 'campo', 'ótimo', 'avaro', 'vasto', 'grupo', 'estão', 'aceso', 'morro', 'antes', 'sinal', 'andar', 'conta', 'lenda', 'reger', 'banzo', 'anais', 'áureo', 'prado', 'verbo', 'acima', 'oxalá', 'opção', 'fugir', 'serão', 'festa', 'chulo', 'segue', 'vilão', 'rapaz', 'leite', 'motim', 'birra', 'nação', 'texto', 'brava', 'treta', 'fruir', 'índio', 'tirar', 'parar', 'fitar', 'átomo', 'ídolo', 'puxar', 'jazia', 'átrio', 'filho', 'alude', 'gerir', 'tenso', 'reino', 'traga', 'tosco', 'prazo', 'prova', 'turba', 'norma', 'bônus', 'exame', 'época', 'manhã', 'voraz', 'acesa', 'corpo', 'preto', 'cheio', 'sarça', 'bando', 'aonde', 'malta', 'ligar', 'arcar', 'nosso', 'magia', 'fatos', 'quase', 'sinhá', 'venal', 'psico', 'anciã', 'cópia', 'avião', 'fatal', 'logro', 'longe', 'certa', 'dessa', 'afora', 'praga', 'quota', 'nível', 'fixar', 'oásis', 'sexta', 'apego', 'mente', 'messe', 'pompa', 'nódoa', 'lidar', 'perda', 'apelo', 'tocar', 'parca', 'alado', 'coito', 'jirau', 'caixa', 'verve', 'glosa', 'sumir', 'fraco', 'livre', 'tinha', 'soldo', 'vezes', 'porta', 'firme', 'lindo', 'grave', 'cânon', 'bater', 'solto', 'opaco', 'faixa', 'irmão', 'astro', 'besta', 'salve', 'sabia', 'virão', 'turva', 'atual', 'doído', 'trupe', 'elite', 'supra', 'navio', 'fenda', 'deixa', 'grata', 'pardo', 'alçar', 'junco', 'autor', 'exijo', 'cioso', 'pique', 'curso', 'parva', 'bioma', 'viria', 'bicho', 'macio', 'douto', 'desta', 'chato', 'aluno', 'ético', 'pagão', 'reses', 'cousa', 'menos', 'ficha', 'calda', 'posto', 'caber', 'abuso', 'rádio', 'vídeo', 'locus', 'culpa', 'supor', 'judeu', 'lápis', 'zelar', 'verba', 'super', 'gosto', 'suave', 'drops', 'calão', 'advir', 'extra', 'retém', 'agudo', 'júlia', 'molho', 'privê', 'torso', 'baixo', 'vosso', 'facho', 'piada', 'peito', 'vinha', 'turma', 'sítio', 'ígneo', 'ruína', 'passa', 'pódio', 'asilo', 'light', 'combo', 'traço', 'órfão', 'ávida', 'estio', 'pilar', 'turvo', 'louça', 'chama', 'mosto', 'ações', 'páreo', 'refém', 'forem', 'amena', 'poeta', 'pisar', 'museu', 'mesma', 'brabo', 'acolá', 'ereto', 'lasso', 'local', 'meigo', 'finda', 'metiê', 'optar', 'medir', 'drama', 'busca', 'teste', 'poema', 'tento', 'cútis', 'clima', 'surja', 'autos', 'facto', 'coral', 'folga', 'rumor', 'aviso', 'cocho', 'geral', 'rouca', 'hobby', 'amiga', 'paira', 'calmo', 'pedra', 'idoso', 'tacha', 'boato', 'cetro', 'feroz', 'urgia', 'volta', 'rubro', 'pacto', 'feudo', 'lição', 'móvel', 'crime', 'açude', 'monge', 'golpe', 'ateia', 'clean', 'daqui', 'artur', 'ecoar', 'riste', 'ponha', 'tetra', 'ébano', 'casar', 'carta', 'corso', 'bença', 'manga', 'natal', 'falha', 'monte', 'aroma', 'saldo', 'cacho', 'verde', 'vigia', 'conto', 'plumo', 'itens', 'escol', 'briga', 'vetar', 'hoste', 'tribo', 'grama', 'fazia', 'pasmo', 'fórum', 'tarde', 'mangá', 'letal', 'amada', 'única', 'ornar', 'pedro', 'troça', 'vento', 'rival', 'chefe', 'sósia', 'súcia', 'civil', 'fruto', 'úteis', 'roupa', 'venha', 'plaga', 'nuvem', 'tchau', 'penta', 'pinho', 'órgão', 'sarau', 'plebe', 'areia', 'átimo', 'jogar', 'swing', 'vazão', 'virar', 'jejum', 'cargo', 'cover', 'nesse', 'arado', 'lesse', 'berro', 'stand', 'seixo', 'macro', 'fosso', 'perto', 'magna', 'axila', 'catre', 'finjo', 'gíria', 'mídia', 'rocha', 'farta', 'beijo', 'tiver', 'varoa', 'légua', 'troca', 'inter', 'tutor', 'bruto', 'tição', 'calor', 'todas', 'bruta', 'traje', 'deste', 'renda', 'gabar', 'close', 'pomar', 'assar', 'trato', 'tenha', 'vadio', 'dança', 'surto', 'porte', 'guria', 'amado', 'santo', 'arfar', 'perco', 'nessa', 'estro', 'viram', 'xucro', 'verão', 'âmbar', 'rural', 'feita', 'silvo', 'nesta', 'odiar', 'logos', 'depor', 'mamãe', 'vista', 'canso', 'aviar', 'laudo', 'canto', 'chula', 'fossa', 'marca', 'bazar', 'vedar', 'negar', 'grota', 'cenho', 'etapa', 'pavor', 'cheia', 'salmo', 'cerca', 'recém', 'bolsa', 'minar', 'ágape', 'densa', 'irado', 'cifra', 'visto', 'clero', 'cinto', 'coroa', 'ferpa', 'régio', 'sofia', 'urdir', 'bucho', 'vagar', 'burra', 'horto', 'letra', 'invés', 'ruído', 'largo', 'molde', 'folha', 'quais', 'segar', 'lesão', 'proto', 'jazer', 'símio', 'sótão', 'esgar', 'paiol', 'pugna', 'final', 'velha', 'úbere', 'penso', 'trago', 'fundo', 'morfo', 'lesto', 'narco', 'pasma', 'vasta', 'deram', 'queda', 'ceita', 'podar', 'álamo', 'olhos', 'ufano', 'ardis', 'troço', 'linha', 'piche', 'apear', 'troco', 'pólis', 'viger', 'úmido', 'preço', 'frota', 'folia', 'bulir', 'áudio', 'mocho', 'neste', 'peita', 'outra', 'ileso', 'farol', 'monta', 'disso', 'resto', 'manto', 'matar', 'cosmo', 'chave', 'seiva', 'redor', 'chaga', 'barro', 'bolso', 'cível', 'falsa', 'mover', 'misto', 'retro', 'vazia', 'lábia', 'limpo', 'louca', 'veloz', 'logia', 'campa', 'nácar', 'bedel', 'nariz', 'barão', 'justa', 'louro', 'mimar', 'banto', 'lutar', 'álbum', 'sabor', 'samba', 'macho', 'dados', 'gemer', 'porca', 'lucro', 'punha', 'axial', 'toque', 'coevo', 'arroz', 'longo', 'zumbi', 'calça', 'enjoo', 'rente', 'salva', 'findo', 'calvo', 'subir', 'venho', 'farto', 'urgir', 'diabo', 'lousa', 'pagar', 'xampu', 'baixa', 'pluma', 'sacar', 'valer', 'sabiá', 'ousar', 'firma', 'sexto', 'bruxa', 'solta', 'forro', 'sigla', 'torna', 'fátuo', 'repor', 'fazes', 'reler', 'lento', 'hífen', 'choça', 'focar', 'gueto', 'fugiu', 'cardo', 'bugre', 'pular', 'corte', 'custo', 'vário', 'corar', 'voilà', 'canil', 'demão', 'feira', 'mania', 'nesga', 'versa', 'rácio', 'míope', 'ferir', 'sadio', 'sócio', 'modal', 'harém', 'tênis', 'tumba', 'digna', 'sugar', 'puído', 'ceifa', 'penca']

random.seed()
termo = palavras[random.randint(0,1000)]

#colocar a palavra secreta em uma lista pq dps da pra verificar a posicao certinha
termo_lista = []
for i in range(0,5):
    termo_lista.extend(termo[i])
print(termo_lista)

#termo sem acento
termo_sa = unidecode(termo)
termo_sa_lista = []
for i in range(5):
    termo_sa_lista.extend(termo_sa[i])
print(termo_sa)


#enquanto o player ainda tem tentativas:
tentativas = 6
while tentativas != 0:
    #inserir tentativa:
    guess = str(input("tentativa: "))

    #se a palavra tiver menos ou mais de 5 letras:
    if len(guess) != 5:
        guess = str(input("digite uma palavra válida: "))

    #colocar a tentativa em uma lista pra verificar as posicao das letras
    guess_lista = []
    for i in range(5):
        guess_lista.extend(guess[i])
   
    tentativas -= 1

   #verificar as posicoes das letra e ver se bate
    for i in range(5):
        #vai ver se as letra da palavra tentada tem na palavra secreta
        if guess_lista[i] in termo_sa_lista:
            #e se tiver vai verificar se ta na posicao certa ou nao
            if guess_lista[i] == termo_sa_lista[i]:
                print(f"{guess_lista[i]} está na posição certa")

            else:
                print(f"{guess_lista[i]} está na posição errada")

    #se a palavra tentada for compativel com a palavra secreta
    if guess_lista == termo_sa_lista:
        print(termo_lista)
        print("Parabéns você ganhou!!!")
        break

    else:
        print(guess_lista)

#quando acaba as tentativas
else:
    print("Você perdeu!!!")

        
