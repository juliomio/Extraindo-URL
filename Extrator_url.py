import re


class Extrator_URL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def __len__(self):
        return len(self.url)

    def __str__(self):
        valor_tot = self.get_valor_parametro('quantidade')
        return f'Quantidade Total de moeda é {valor_tot} \n' \
               f'A URl contem {len(self.url)} caracteres'

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return None

    def valida_url(self):
        if not self.url or not self.url.startswith('https://'):
            raise ValueError('URL vazia ou Inválida !!')

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError('URL vazia ou invalida !')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[0:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        moeda_dest = 'moeda destino'
        moeda_dest1 = self.url.find('moedaDestino') + len(moeda_dest)
        final_moeda_dest1 = self.url.find('&', moeda_dest1)
        extrai_moeda_dest1 = self.url[moeda_dest1:final_moeda_dest1]

        moeda_ori = 'moeda origem'
        moeda_ori1 = self.url.find('moedaOrigem') + len(moeda_ori)
        final_moeda_ori1 = self.url.find('&', moeda_ori1)
        extrai_moeda_ori1 = self.url[moeda_ori1:final_moeda_ori1]

        quantidade = 'quantidade'
        quant1 = self.url.find('quantidade') + len(quantidade) + 1
        extrai_quantidade = self.url[quant1:]

        if parametro_busca == moeda_dest:
            return 'Moeda Destino: {}'.format(extrai_moeda_dest1)
        elif parametro_busca == moeda_ori:
            return 'Moeda Origem: {}'.format(extrai_moeda_ori1)
        elif parametro_busca == quantidade:
            return ': {}'.format(extrai_quantidade)







#Verificando o Funcionamento do Programa ...

url = "https://bytebank.com/cambio?moedaDestino=libras&moedaOrigem=real&quantidade=300"
extai_url = Extrator_URL(url)
valor_buscado = extai_url.get_valor_parametro('moeda destino')
print(extai_url)
print(valor_buscado)


