alunos= input()
a=raw_input()
vetor= map(int, a.split())
vetor2=[1]*(len(vetor))
vetor.sort()
print vetor



seen = set()
uniq = []
for x in a:
    if x not in seen:
        uniq.append(x)
        seen.add(x)


print seen
print uniq


