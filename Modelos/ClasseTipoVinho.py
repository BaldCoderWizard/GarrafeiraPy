from PreparacaoDataBase.GarrafeiraBD import Database
import re

class TipoVinho(Database):
    def __init__(self, tipovinho="", descricao=""):
        super().__init__()
        self.tipovinho = tipovinho
        self.descricao = descricao


    def validacao_tipo(self, tipovinho):
        padrao = r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s'-]+$"
        if re.match(padrao, tipovinho):
            return True
        else:
            return False
        
    def validacao_descricao(self, descricao):
        padrao = r"^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ,.!?'\":;()-][a-zA-Z0-9áàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ\s,.!?'\":;()-]*$"
        if re.match(padrao, descricao):
            return True
        else:
            return False

    def validacao_id(self, idtipovinho):
        padrao = r"^[1-9]\d*$"
        if re.match(padrao, idtipovinho):
            return True
        else:
            return False
    
    def adicionar_tipovinho(self, tipovinho, descricao):
        try:
            query = " INSERT INTO TipoVinho (TipoVinho, Descricao)  VALUES (%s, %s)"
            self.cursor.execute(query, (tipovinho, descricao,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar Tipo de Vinho {e}")
        return False

    def visualizar_tipo(self):
        query = "SELECT * FROM TipoVinho"
        self.cursor.execute(query)
        tipos = self.cursor.fetchall()
        return tipos
    
    def eliminar_tipo(self, idtipovinho):
        try:
            query = "Delete from TipoVinho where IdTipoVinho = %s"
            self.cursor.execute(query, (idtipovinho,))
            if self.cursor.rowcount == 0:
                print("Nenhum tipo de vinho encontrado com esse ID.")
            else:
                self.connection.commit()
                print("Tipo de vinho eliminado.")
        except Exception as e:
            print(f"Erro ao apagar Tipo de vinho: {e}")
