from PreparacaoDataBase.GarrafeiraBD import Database
import re

class Produtor(Database):
    
    def __init__(self, nome='', id_regiao=0, telefone=0, website='', email=''):
        super().__init__()
        self.nome = nome
        self.id_regiao = id_regiao
        self.telefone = telefone
        self. website = website
        self. email = email

    def validacao_id(self, id):
        padrao = r"^[1-9]\d*$"
        if re.match(padrao, id):
            return True
        else:
            return False

    def validacao_nome(self, nome):
        padrao = r'^[a-zA-ZáàâãéèêíïóôõöúçñÁÀÂÃÉÈÊÍÏÓÔÕÖÚÇÑ ]+$'
        if re.match(padrao, nome):
            return True
        else:
            return False

    def validacao_telefone(self, telefone):
        padrao = r'^(2|9)\d{8}$'
        if re.match(padrao, telefone):
            return True
        else:
            return False
        
    def validacao_email(self, email):
        padrao = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(padrao, email):
            return True
        else:
            return False
    
    def validacao_website(self, website):
        padrao = r'^(https?://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/.*)?$'
        if re.match(padrao, website):
            return True
        else:
            return False

    def adicionar_produtor(self, nome, id_regiao, telefone, website, email):
        try:
            query = """
            INSERT INTO Produtor (Nome, IdRegiao, Telefone, Website, Email) 
            VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (nome, id_regiao, telefone, website, email))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar o Produtor: {e}")
            return False
    
    def visualizar_produtores(self):
        query = "SELECT * FROM Produtor"
        self.cursor.execute(query)
        produtor = self.cursor.fetchall()
        return produtor
    
    def eliminar_produtor(self, id_produtor):
        try:
            query = "DELETE FROM Produtor Where IdProdutor = %s"
            self.cursor.execute(query, (id_produtor,))
            self.connection.commit()
            return True  
        except Exception as e:
            print(f"Erro ao eliminar Produtor: {e}")
            return False

    def atualizar_produtor(self, id_produtor, novo_nome, novo_telefone, novo_website, novo_email):
        try:
            query = """
            UPDATE Produtor 
            SET Nome = %s, Telefone = %s, Website = %s, Email = %s
            WHERE IdProdutor = %s
            """
            self.cursor.execute(query, (novo_nome, novo_telefone, novo_website, novo_email, id_produtor))
            self.connection.commit()
            return True  
        except Exception as e:
            print(f"Erro ao atualizar Produtor: {e}")
            return False 

        


