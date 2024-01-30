
1 parent 3ef37fd
commit c8dfa22
Showing 1 changed file with 20 additions and 0 deletions.
 20 changes: 20 additions & 0 deletions20  
aula31.py
@@ -0,0 +1,20 @@
"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')


if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')