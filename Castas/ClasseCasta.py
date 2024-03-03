from PreparacaoDataBase.GarrafeiraBD import Database
import re

class Casta(Database):
    def __init__(self, casta=0, descricao=""):
        super().__init__()
        self.casta = casta
        self.descricao = descricao


    def validacao_casta(self, casta):
        padrao = r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s'-]+$"
        if re.match(padrao, casta):
            return True
        else:
            return False
    
    def validacao_descricao(self, descricao):
        padrao = r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ,.!?'\":;()-][a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s,.!?'\":;()-]*$"
        if re.match(padrao, descricao):
            return True
        else:
            return False

    def adicionar_casta(self, casta, descricao):
        try:
            query = " INSERT INTO Casta (Casta, Descricao)  VALUES (%s, %s)"
            self.cursor.execute(query, (casta, descricao,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar Casta {e}")
        return False

    def visualizar_casta(self):
        query = "SELECT * FROM Casta"
        self.cursor.execute(query)
        castas = self.cursor.fetchall()
        return castas
    
    def apagar_casta(self, idcasta):
        query = "Delete from Casta where IdCasta = %s"
        self.cursror.execute(query, (idcasta,))
        self.connection.commit()

        
