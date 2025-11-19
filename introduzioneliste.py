#creare coppie di nomi combinando due liste: una di nomi maschili e una di nomi femminili

maschili = ['mario', 'luigi', 'pippo', 'pluto']
femminili = ['minnie', 'topolina', 'paperina', 'paperoga']

lista=[[i, j]for i in maschili for j in femminili]
print(lista)

