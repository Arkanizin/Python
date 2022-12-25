natal = str(input ('Hoje ê natal ?[S/N]')).strip().upper()[0]
while natal not in 'SsNn':
	natal = str(input('Informação incorrera. Hoje ê natal?[S/N]' )).strip().upper()[0]
	
if natal == 'S':
	print('☆'.center(40))
	
	for i in range(1,40,2):
	    print(('*'*i).center(40))
	for i in range(3):
	    print('||'.center(40))
	print('\.\==============/./'.center(40))
	print()
	print('Feliz Natal e que deus elimine a todos vocês!',end='\n\n')
	input('made stein')
	input()
	
	
if natal == 'N':
	print('Que pena. Va para o inferno')
