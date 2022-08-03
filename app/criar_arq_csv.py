import os


class GerarArquivoCsv:

    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.local_arquivo = os.path.join(os.getcwd(), r'new_file\HIST_PAINEL_COVIDBR.csv')

    def gerar_csv(self):
        # Criando arquivo CSV
        self.dataframe.to_csv(self.local_arquivo, sep=';', index=False, encoding='utf-8-sig')
        print('Arquivo criado com sucesso.')
