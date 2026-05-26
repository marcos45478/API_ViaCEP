import pytest
import requests

# Fixture de sessão
@pytest.fixture(scope='session')
def api_client():
    return requests.Session()

# Fixture de função
@pytest.fixture(scope='function')
def api_url():
    return "https://viacep.com.br/ws/"

#CT-01
def test_cep_valido(api_client, api_url):
    response = api_client.get(f"{api_url}/01001000/json/")
    
    assert response.status_code == 200
    data = response.json()
    
    assert data['logradouro'] == "Praça da Sé"
    assert data['bairro'] == "Sé"
    assert data['localidade'] == "São Paulo"
    assert data['uf'] == "SP"
    
#CT-02
def test_cep_com_hifen(api_client, api_url):
    response = api_client.get(f"{api_url}/01001-000/json/")
    data = response.json()
    assert response.status_code == 200
    assert "logradouro" in data
    
#CT-03
def test_cep_invalido(api_client, api_url):
    response = api_client.get(f"{api_url}/99999999/json/")
    data = response.json()
    assert response.status_code == 200
    assert 'erro' in data
    
#CT-04
def test_cep_com_letras(api_client, api_url):
    response = api_client.get(f"{api_url}ABCDEFGH/json/")
    assert response.status_code in [400, 200]
    
#CT-05
def test_cep_incompleto(api_client, api_url):
    response = api_client.get(f"{api_url}12345/json/")
    assert response.status_code in [400, 200]

#CT-06    
def test_cep_vazio(api_client, api_url):
    response = api_client.get(f"{api_url}/json/")
    assert response.status_code in [400, 200]