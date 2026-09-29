"""Reproduce ejemplos didácticos de la sesión 10. Solo biblioteca estándar."""
from fractions import Fraction as F
from math import ceil
ranks=[1,2,4,5,None,1,3,None]
def metrics(ranks,k):
 hits=sum(r is not None and r<=k for r in ranks)
 rr=sum((F(1,r) for r in ranks if r is not None and r<=k),F(0))
 return F(hits,len(ranks)),rr/len(ranks)
assert metrics(ranks,3)==(F(1,2),F(17,48))
assert metrics(ranks,5)==(F(3,4),F(197,480))
for k in [3,5]:
 h,m=metrics(ranks,k)
 assert 0<=m<=h<=1
 print(f'k={k}: Hit Rate={float(h):.4f}; MRR={float(m):.4f} ({m})')
new=ranks.copy();new[2]=2
assert metrics(new,5)[0]==metrics(ranks,5)[0]
assert metrics(new,5)[1]-metrics(ranks,5)[1]==F(1,32)
assert metrics([1,3,5,None],3)==(F(1,2),F(1,3))
assert metrics([1,3,5,None],5)==(F(3,4),F(23,60))
assert F(126,900)==F(14,100)
assert F(126,300)==F(42,100)
L,C,O=500,126,26
n=1+ceil((L-C)/(C-O))
lengths=[min(C,L-i*(C-O)) for i in range(n)]
assert lengths==[126,126,126,126,100]
assert sum(lengths)==604
rrf={'A':F(1,61),'B':F(1,62)+F(1,61),'C':F(1,62)}
assert sorted(rrf,key=rrf.get,reverse=True)==['B','A','C']
assert sum([10,35,10,10,10,10,5,10])==100
print('Verificados: reranking, ejercicios, truncamiento, solapamiento, RRF y pesos.')
