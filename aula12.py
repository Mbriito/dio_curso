import requests
# via cep
def retorna_dado_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
    print(response.status_code)
    print(response.json())
    dado_cep = response.json ()
    print(type(response.json()))
    print(dado_cep['logradouro'])
    print(dado_cep['complemento'])
    return dado_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' .format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):  # retorna o html da pagina
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    #retorna_dado_cep('01001000')
    dados_pokemon = retorna_dados_pokemon('pikachu')
    print(dados_pokemon['sprites']['front_shiny'])          # retorna o link da imagem do pokemon retiraddo do codigo json em sprites
    #response = retorna_response('https://digitalinnovation.one/')  #retorna html da pagian
    #print(response)
