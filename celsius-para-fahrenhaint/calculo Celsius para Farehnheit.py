#conversão de Celsius para Fahrenhaint

#No código logo abaixo...
#será solicitado um valor do tipo decimal (float). Esse valor é referente a temperatura em graus celsius.
#Esse valor será armazenado na variável 'C' que significa Celsius.

C= float(input('Digite a temperatura em graus celsius: '))

#No comando abaixo será executado o cálculo de conversão de graus celsius para fahrenhaint.
#A várial 'F' irá armazenar o resultado desse cálculo.
#Para executar a conversão devemos utilizar a fórmula (C * 1.8 + 32).
#Ou seja, o valor celsius que está na variável 'C' será multiplicado por '1.8', mais (+) 32.

F = (C * 1.8 + 32)

#Por fim, o resultado desse calculo irá aparecer na tela.
print (('O resultado da conversão é de',F,'para graus fahrenhaint'))

