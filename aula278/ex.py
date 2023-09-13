from datetime import datetime
from dateutil.relativedelta import relativedelta

fmt = "%d/%m/%Y"
valor_dev = 1000000
data_inicial = datetime.strptime("20/12/2020", fmt)
dia_venc = 20
prazo_anos = 5
prazo = relativedelta(years=prazo_anos)

data_final = data_inicial+prazo

datas = [data_inicial + relativedelta(months=1)]

while(datas[-1] != data_final):
    datas.append(datas[-1] + relativedelta(months=1))

num_parcelas = len(datas)
valor_parcela = valor_dev / num_parcelas

for data_venc in datas:
    print(f"Data vencimento: {data_venc.strftime(fmt)}. Parcela: R$ {valor_parcela:.2f}")

'''
if(__name__ == "__main__"):
    print(data_inicial.strftime(fmt))
    print(prazo)
    print(data_final.strftime(fmt))
    print(datas[-1].strftime(fmt))
    print(f"{valor_parcela:.2f}")
'''