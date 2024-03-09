listaZakupy=["temerska",69,6.9,"fisstech","temerska",6.9,6.9]
slownikListy={}
for i in range(len(listaZakupy)):
    slownikListy.update({listaZakupy[i]:listaZakupy.count(listaZakupy[i])})
for j in slownikListy:
    if not (type(j)==float or type(j)==int):
