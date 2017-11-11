alunos= input()
a=raw_input()
vetor= map(int, a.split())
print max(set(vetor), key=vetor.count)
