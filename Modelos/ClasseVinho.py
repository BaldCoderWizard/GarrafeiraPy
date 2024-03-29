from PreparacaoDataBase.GarrafeiraBD import Database
import re
from datetime import datetime

class Vinho(Database):
    def __init__(self, nome="", ano=0, id_produtor=0, id_regiao=0, id_tipo_vinho=0, preco=0.0, quantidade=0):
        super().__init__()
        self.nome = nome
        self.ano = ano
        self.preco = preco
        self.id_produtor = id_produtor
        self.id_tipo_vinho = id_tipo_vinho
        self.id_regiao = id_regiao
        self.quantidade = quantidade

    def validacao_nome(self, nome):
        padrao = r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s'-]+$"
        if re.match(padrao, nome):
            return True
        else:
            return False
        
    def validacao_ano(self, ano):
        padrao = r"^(19|20)\d{2}$"
        if not re.match(padrao, str(ano)):
            print(f"Deve inserir um ano entre 1900 e {datetime.now().year}")
            return False
        ano = int(ano)
        ano_atual = datetime.now().year
        if ano <= ano_atual and ano >= 1900:
            return True
        else:
            print(f"Deve inserir um ano entre 1900 e {ano_atual} ")
            return False
        
    def validacao_preco(self, preco):
        padrao = r"^\d+(\.\d{1,2})?$"
        if re.match(padrao, preco):
            return True
        else:
            return False
    
    def validacao_quantidade(self, quantidade):
        padrao = r"^\d+$"
        if re.match(padrao, quantidade):
            return True
        else:
            return False
    

    def adicionar_vinho(self, nome, ano, id_produtor, id_regiao, id_tipo_vinho, preco, quantidade):
        try:
            query = """
            INSERT INTO Vinho (Nome, Ano, IdProdutor, IdRegiao, IdTipoVinho, Preco, Quantidade) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, ano, id_produtor, id_regiao, id_tipo_vinho, preco, quantidade,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar Vinho: {e}")
        return False

    def visualizar_vinho(self):
        query = """Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, produtor.Nome as NomeProdutor, regiao.Regiao as NomeRegiao, tipovinho.TipoVinho as TipoVinho, vinho.Quantidade as Quantidade, vinho.Preco as Preco from vinho
                inner join produtor on vinho.IdProdutor = produtor.IdProdutor
                inner join regiao on vinho.IdRegiao = regiao.IdRegiao 
                inner join tipovinho on vinho.IdTipoVinho = tipovinho.IdTipoVinho
                order by vinho.IdVinho
                """
        self.cursor.execute(query)
        vinhos = self.cursor.fetchall()
        return vinhos
    
    def eliminar_vinho(self, IdVinho):
        try:
            query = "DELETE FROM Vinho Where IdVinho = %s"
            self.cursor.execute(query, (IdVinho,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao eliminar o Vinho: {e}")
        return False

    def atualizar_stock_vinho(self, idvinho, quantidade):
        try:
            query = "UPDATE Vinho SET quantidade = %s WHERE IdVinho = %s"        
            self.cursor.execute(query, (quantidade, idvinho))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao atualizar Stock: {e}")
        return False
    
    def visualizar_vinho_stock(self):
        query = """Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, produtor.Nome as NomeProdutor, regiao.Regiao as NomeRegiao, tipovinho.TipoVinho as TipoVinho, vinho.Quantidade as Quantidade, vinho.Preco as Preco from vinho
                inner join produtor on vinho.IdProdutor = produtor.IdProdutor
                inner join regiao on vinho.IdRegiao = regiao.IdRegiao 
                inner join tipovinho on vinho.IdTipoVinho = tipovinho.IdTipoVinho
                where vinho.Quantidade > 0
                order by vinho.Quantidade   
                """        
        self.cursor.execute(query)
        vinhos = self.cursor.fetchall()
        return vinhos
    
    def visualizar_vinho_semstock(self):
        query = """Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, produtor.Nome as NomeProdutor, regiao.Regiao as NomeRegiao, tipovinho.TipoVinho as TipoVinho, vinho.Quantidade as Quantidade, vinho.Preco as Preco from vinho
                inner join produtor on vinho.IdProdutor = produtor.IdProdutor
                inner join regiao on vinho.IdRegiao = regiao.IdRegiao 
                inner join tipovinho on vinho.IdTipoVinho = tipovinho.IdTipoVinho
                where vinho.Quantidade = 0
                order by vinho.IdVinho   
                """           
        self.cursor.execute(query)
        vinhos = self.cursor.fetchall()
        return vinhos

    def visualizar_vinho_ano(self, ano =''):
        query = """Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, produtor.Nome as NomeProdutor, regiao.Regiao as NomeRegiao, tipovinho.TipoVinho as TipoVinho, vinho.Quantidade as Quantidade, vinho.Preco as Preco from vinho
                inner join produtor on vinho.IdProdutor = produtor.IdProdutor
                inner join regiao on vinho.IdRegiao = regiao.IdRegiao 
                inner join tipovinho on vinho.IdTipoVinho = tipovinho.IdTipoVinho
                where ano = %s
                order by vinho.IdVinho   
                """
        self.cursor.execute(query, (ano,))
        vinhos = self.cursor.fetchall()#o fetchall para quando vamos buscar dados
        return vinhos
    
    def visualizar_vinho_nome(self, string =''):
        procurarstring = f"%{string}%"
        query = """Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, produtor.Nome as NomeProdutor, regiao.Regiao as NomeRegiao, tipovinho.TipoVinho as TipoVinho, vinho.Quantidade as Quantidade, vinho.Preco as Preco from vinho
                inner join produtor on vinho.IdProdutor = produtor.IdProdutor
                inner join regiao on vinho.IdRegiao = regiao.IdRegiao 
                inner join tipovinho on vinho.IdTipoVinho = tipovinho.IdTipoVinho
                where vinho.Nome like %s
                order by vinho.IdVinho   
                """
        self.cursor.execute(query, (procurarstring,))
        vinhos = self.cursor.fetchall()
        return vinhos
    



    