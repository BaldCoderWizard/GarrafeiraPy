from PreparacaoDataBase.GarrafeiraBD import Database

class VinhoCasta(Database):
    def __init__(self, idvinho=0, idcasta=0):
        super().__init__()
        self.idvinho = idvinho
        self.idcasta = idcasta

    def adicionar_casta_vinho(self, idvinho, idcasta):
        try:
            query = "INSERT INTO vinhocasta (IdVinho, IdCasta) VALUES (%s, %s)"
            self.cursor.execute(query, (idvinho, idcasta,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao adicionar casta ao vinho: {e}")
            return False

    def remover_casta_vinho(self, idvinho, idcasta):
        try:
            query = "DELETE FROM vinhocasta WHERE IdVinho = %s AND IdCasta = %s"
            self.cursor.execute(query, (idvinho, idcasta,))
            self.connection.commit()
            return True
        except Exception as e:
            print(f"Erro ao remover casta do vinho: {e}")
            return False
        
    def visualizar_todos(self):
        try:
            query = """
            Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, GROUP_CONCAT(casta.Casta ORDER BY casta.Casta SEPARATOR ', ') AS Castas FROM vinho
            INNER JOIN vinhocasta ON vinho.IdVinho = vinhocasta.IdVinho
            INNER JOIN casta ON vinhocasta.IdCasta = casta.IdCasta
            GROUP BY vinho.IdVinho, vinho.Nome;
            """
            self.cursor.execute(query)
            todos = self.cursor.fetchall()
            return todos
        except Exception as e:
            print(f"Erro ao listar Vinhos e Castas: {e}")
            return []
        
    def visualizar_casta_vinho(self, idvinho):
        try:
            query = """ 
            Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, tipovinho.TipoVinho as TipoVinho, GROUP_CONCAT(casta.Casta ORDER BY casta.Casta SEPARATOR ', ') AS Castas FROM vinho
            INNER JOIN vinhocasta ON vinho.IdVinho = vinhocasta.IdVinho 
            INNER JOIN tipovinho ON vinho.IdTipoVinho = tipovinho.IdTipoVinho 
            INNER JOIN casta ON vinhocasta.IdCasta = casta.IdCasta
            where vinho.IdVinho = %s
            GROUP BY vinho.IdVinho, vinho.Nome;
            """
            self.cursor.execute(query, (idvinho,))
            castas = self.cursor.fetchall()
            return castas
        except Exception as e:
            print(f"Erro ao listar as castas do vinho: {e}")
            return []
    
    def visualizar_vinho_casta(self, string=""):
        try:
            procurarstring = f"%{string}%"
            query = """
            Select vinho.IdVinho as IdVinho, vinho.Nome as NomeVinho, vinho.Ano as AnoVinho, tipovinho.TipoVinho as TipoVinho FROM vinho
            INNER JOIN vinhocasta ON vinho.IdVinho = vinhocasta.IdVinho 
            INNER JOIN tipovinho ON vinho.IdTipoVinho = tipovinho.IdTipoVinho 
            INNER JOIN casta ON vinhocasta.IdCasta = casta.IdCasta
            where casta.Casta like %s
            GROUP BY vinho.IdVinho, vinho.Nome;
            """
            self.cursor.execute(query, (procurarstring,))
            vinhos = self.cursor.fetchall()
            return vinhos
        except Exception as e:
            print(f"Erro ao listar os vinhos por casta: {e}")
            return []