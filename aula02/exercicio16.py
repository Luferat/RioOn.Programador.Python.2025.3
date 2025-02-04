'''
Exercício 16
Alerta Climático: pergunte se está chovendo e se há previsão de raios. 
 - Se estiver chovendo e houver previsão de raios, exiba "Fique em casa!". 
 - Se apenas um dos fatores for verdadeiro, exiba "Cuidado ao sair". 
 - Caso contrário, exiba "Pode sair com segurança". 
'''

# Pergunta se está chovendo
chovendo = input("Está chovendo? (sim/não): ").strip().lower() == "sim"

# Pergunta se há previsão de raios
previsao_raios = input("Há previsão de raios? (sim/não): ").strip().lower() == "sim"

# Verifica as condições e exibe o resultado
if chovendo and previsao_raios:
    print("Fique em casa!")
elif chovendo or previsao_raios:
    print("Cuidado ao sair")
else:
    print("Pode sair com segurança")
