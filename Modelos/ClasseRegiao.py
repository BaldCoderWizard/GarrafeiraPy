from PreparacaoDataBase.GarrafeiraBD import Database
import re

class Regiao(Database):
    def __init__(self, regiao=''):
        super().__init__()
        self.regiao = regiao

    def validacao_id(self, idregiao):
        padrao = r"^[1-9]\d*$"
        if re.match(padrao, idregiao):
            return True
        else:
            return False

    def validacao_regiao(self, regiao):
        padrao = r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s'-]+$"
        if re.match(padrao, regiao):
            return True
        else:
            return False

    def regiao_existe(self, regiao):
        query = "SELECT COUNT(*) FROM Regiao WHERE IdRegiao = %s"
        self.cursor.execute(query, (regiao,))
        resultado = self.cursor.fetchone()
        if resultado['COUNT(*)'] > 0:
            return True
        else:
            return False

    def adicionar_regiao(self, regiao):
        if self.regiao_existe(regiao):
            print("Erro: A região já existe.")
            return False  
        try:
            query = "INSERT INTO Regiao (Regiao) VALUES (%s)"
            self.cursor.execute(query, (regiao,))
            self.connection.commit()
            print("Regiao adicionada com sucesso.")
            return True
        except Exception as e:
            print(f"Erro ao adicionar região: {e}")
            return False
        
    def atualizar_regiao(self, id_regiao, nova_regiao):
        try:
            query = """
            UPDATE Regiao 
            SET Regiao = %s
            WHERE IdRegiao = %s
            """
            self.cursor.execute(query, (nova_regiao, id_regiao))
            self.connection.commit()
            return True  
        except Exception as e:
            print(f"Erro ao atualizar Regiao: {e}")
            return False 

    
    def visualizar_regiao(self):
        query = "SELECT * FROM Regiao Order by IdRegiao"
        self.cursor.execute(query)
        regioes = self.cursor.fetchall()
        return regioes
    
    def apagar_regiao(self, idregiao):
        try:
            query = "DELETE from Regiao Where IdRegiao =%s"
            self.cursor.execute(query, (idregiao,))
            if self.cursor.rowcount == 0:
                print("Nenhuma regiao encontra com esse ID.")
            else:
                self.connection.commit()
                print("Regiao apagada com sucesso.")
        except Exception as e:
            print(f"Erro ao apagar regiao: {e}")


    