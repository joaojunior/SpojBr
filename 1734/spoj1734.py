def ordena(lista):
    return sorted(lista,key=lambda aluno:(aluno[1]*-1,aluno[0]),reverse=True)

def calculaAlunoAprovado(alunos):
    aluno_reprovado = ordena(alunos)[0][0]
    return aluno_reprovado
    
def imprime_resposta(instancia,aluno):
    print "Instancia",instancia
    print aluno

def main():
    instancia = 0
    while(True):
        menor_nota = 11
        try:
            instancia += 1
            quantidade = int(raw_input())
            for i in xrange(quantidade):
                aluno = raw_input()
                aluno = aluno.split(" ")
                nota = int(aluno[1])
                if nota < menor_nota:
                    menor_nota = nota
                    nome = aluno[0]
                elif nota == menor_nota:
                    if aluno[0] > nome:
                        nome = aluno[0]
            imprime_resposta(instancia,nome)
        except EOFError:
            break
main()
