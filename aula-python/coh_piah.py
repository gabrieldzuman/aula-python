import re

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = [separa_frases(sentenca) for sentenca in sentencas]
    palavras = [separa_palavras(frase) for frase in sum(frases, [])]

    total_palavras = sum(len(frase) for frase in palavras)
    total_sentencas = len(sentencas)
    total_frases = sum(len(sentenca) for sentenca in frases)

    tam_medio_palavra = sum(len(palavra) for frase in palavras for palavra in frase) / total_palavras
    type_token = len(set(word.lower() for sentence in palavras for word in sentence)) / total_palavras
    hapax_legomana = len([word for sentence in palavras for word in sentence if palavras.count(word) == 1]) / total_palavras
    tam_medio_sentenca = sum(len(sentenca) for sentenca in sentencas) / total_sentencas
    complexidade_sentenca = total_frases / total_sentencas
    tam_medio_frase = sum(len(frase) for sentenca in frases for frase in sentenca) / total_frases

    return [tam_medio_palavra, type_token, hapax_legomana, tam_medio_sentenca, complexidade_sentenca, tam_medio_frase]

def compara_assinatura(as_a, as_b):
    similaridade = 0
    for i in range(len(as_a)):
        similaridade += abs(as_a[i] - as_b[i])
    return similaridade / 6

def avalia_textos(textos, ass_cp):
    assinaturas_textos = [calcula_assinatura(texto) for texto in textos]
    similaridades = [compara_assinatura(assinatura, ass_cp) for assinatura in assinaturas_textos]
    texto_infectado_index = similaridades.index(min(similaridades))
    return texto_infectado_index + 1

def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    return frase.split()

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho médio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

if __name__ == "__main__":
    assinatura_infectado = le_assinatura()
    textos = le_textos()
    texto_infectado_index = avalia_textos(textos, assinatura_infectado)
    print(f"O autor do texto {texto_infectado_index} está infectado com COH-PIAH")
