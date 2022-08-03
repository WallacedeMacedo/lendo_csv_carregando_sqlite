import sqlite3
import os


class DataBaseSqlite:

    def __init__(self, dataframe):
        self.dframe = dataframe

    def insert_into(self):
        conn = None
        cursor = None
        try:
            local_database = os.path.join(os.getcwd(), 'database')
            conn = sqlite3.connect(os.path.join(local_database, 'db_covid.db'))
            cursor = conn.cursor()
            print(os.path.join(local_database, 'db_covid.db'))

            create_table = '''
            create table if not exists covid
            ('regiao' text,
            'estado' text,
            'municipio' text,
            'coduf' integer,
            'codmun' integer,
            'codregiaosaude' integer,
            'nomeregiaosaude' text,
            'data' text,
            'semanaepi' integer,
            'populacaoTCU2019' integer,
            'casosacumulado' integer,
            'casosnovos' integer,
            'obitosacumulado' integer,
            'obitosnovos' integer,
            'recuperadosnovos' integer,
            'emacompanhamentonovos' integer,
            'interiormetropolitana' integer,
            PRIMARY KEY (coduf, codmun, data, semanaepi)
            )'''

            # Inserindo ',' entre as colunas do dataframe.
            colunas = "','".join([str(i) for i in self.dframe.columns.tolist()])

            # Executando o script da tabela
            cursor.execute(create_table)

            # Criando a estrutura do insert
            sql = "insert into covid ('" + colunas + "') values " \
                                                     "(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
            # Transformando as linhas em uma tupla
            insert_dataframe = [tuple(dados) for dados in self.dframe.values]

            # Inserindo os dados
            cursor.executemany(sql, [dados for dados in insert_dataframe])

            # Comitando
            conn.commit()

        except Exception as err:
            print('Erro ao conectar no banco de dados')
            print(err)
        finally:

            if conn:
                # Fechando o cursor
                cursor.close()

                # Fechando a conexão
                conn.close()
        print("Fim da execução!")
