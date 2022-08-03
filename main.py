from app.buscar_arquivo_csv import SelecionarArquivo
from app.database_sqlite import DataBaseSqlite
from app.criar_arq_csv import GerarArquivoCsv
from datetime import datetime


def controle():

    print(datetime.today())

    arquivo = SelecionarArquivo()  # Passando a classe para um objeto
    dframe = arquivo.selecionar_csv()  # Chamando o metodo e retornando o DataFrame

    saida_csv = GerarArquivoCsv(dframe)
    saida_csv.gerar_csv()

    db_sqlite = DataBaseSqlite(dframe)
    db_sqlite.insert_into()

    print(datetime.today())


if __name__ == '__main__':
    controle()
