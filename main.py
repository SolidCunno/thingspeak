import requests

#solidcunno
# config do thingspeak:
# FAVOR NÃO MECHER NO CÓDIGO!

API_THING = 'RWEYWWUMN0K1IVJN'
THINGSPEAK_URL = 'https://api.thingspeak.com/update?api_key=RWEYWWUMN0K1IVJN&field1=0'

def enviar_dados_paciente(nome, rg, data, diagnostico):
    payload = {
        'api_key': API_THING,
        'field1': nome,
        'field2': rg,
        'field3': data,
        'field4': diagnostico
    }
    response = requests.post(THINGSPEAK_URL, data=payload)
    if response.status_code == 200:
        print('Dados enviados com sucesso!')
    else:
        print('Falha ao enviar dados. Código de status:', response.status_code)

# aqui vocês mudam o que está em aspas para cada pessoa
enviar_dados_paciente('João_Silva', '123456789', '05/06/2024', 'Hipertensao')

# Lembrando que, se retornar código 400, não enviou e deu erro. 
# Código 200 sempre! 
