import os
import pandas as pd
from datetime import datetime


class SelecionarArquivo:

    def __init__(self):
        self.dataframe = None
        self.lst_arquivos = []
        self.local = os.path.join(os.getcwd(), 'files')
        self.local_arq = os.path.join(self.local, 'HIST_PAINEL_COVIDBR.csv')
        print('Variávais criadas')

    def selecionar_csv(self):

        ano = datetime.today().strftime("%Y")

        # Buscando arquivo(s) no diretório informado
        for diretorio, pastas, arquivos in os.walk(self.local):
            for arquivo in arquivos:
                if f'_{ano}_' in arquivo:
                    dir_arq = os.path.join(self.local, arquivo)
                    self.lst_arquivos.append(dir_arq)

        print(self.lst_arquivos)

        # Criando o DataFrame
        df = pd.DataFrame()

        # Lendo os dados e adicionando ao dataframe
        for ler in self.lst_arquivos:
            frames = pd.read_csv(ler, delimiter=';')
            df = pd.concat([df, frames], ignore_index=True)

        # Ajustando o nome das colunas
        self.dataframe = df.rename(
            columns={'codRegiaoSaude': 'codregiaosaude', 'nomeRegiaoSaude': 'nomeregiaosaude',
                     'semanaEpi': 'semanaepi', 'casosAcumulado': 'casosacumulado', 'casosNovos': 'casosnovos',
                     'obitosAcumulado': 'obitosacumulado', 'obitosNovos': 'obitosnovos',
                     'Recuperadosnovos': 'recuperadosnovos', 'emAcompanhamentoNovos': 'emacompanhamentonovos',
                     'interior/metropolitana': 'interiormetropolitana'
                     })
        return self.dataframe
