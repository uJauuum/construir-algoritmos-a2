import datetime
import requests


def cotar():
    hoje = datetime.date.today()

    for i in range(365):
        dia = hoje - datetime.timedelta(days=i)

        data_formatada = dia.strftime("%m-%d-%Y")

        url = (
            "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
            f"CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data_formatada}'"
            "&$top=100&$format=json"
        )

        resposta = requests.get(url)

        if resposta.status_code == 200:
            dados = resposta.json()["value"]

            if dados:
                for cotacao in dados:
                    print(
                        dia,
                        "Compra:",
                        cotacao["cotacaoCompra"]
                    )
            else:
                print(dia, "Sem cotação disponível")
        else:
            print(dia, "Erro na consulta:", resposta.status_code)