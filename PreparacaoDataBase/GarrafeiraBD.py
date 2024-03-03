import pymysql

class Database:

    db_iniciada = False

    def __init__(
        self,
        host="localhost",
        user="root",
        password="root",
        database="GarrafeiraPessoal",
    ):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            passwd=password,
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.cursor = self.connection.cursor()
        self.create_database(database)
        self.connection.select_db(database)

    def create_database(self, database_name):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS `{database_name}`;")
            if not Database.db_iniciada:
                print(f"A Base de Dados `{database_name}` foi criada ou ja existe.")
                Database.db_iniciada = True
        except pymysql.Error as e:
            print(f"Erro ao criar a Base de Dados `{database_name}`: {e}")

    # Vinho: IdVinho, Nome, Ano, IdProdutor, IdRegiao, IdTipoVinho, Preco, Quantidade
    def criar_tabelas(self):
        self.CriarTabelaRegiao()
        self.CriarTabelaProdutor()
        self.CriarTabelaCasta()
        self.CriarTabelaTipoVinho()
        self.CriarTabelaVinho()
        self.CriarTabelaVinhoCasta()

    def CriarTabelaRegiao(self):
        try:
            c = self.cursor.execute(
                """
            CREATE TABLE Regiao (
            IdRegiao INT AUTO_INCREMENT PRIMARY KEY,
            Regiao VARCHAR(255) NOT NULL UNIQUE );
                """
            )
            self.connection.commit()
            return (True, None)
        except Exception as error:
            return (False, str(error))

    def CriarTabelaProdutor(self):
        try:
            c = self.cursor.execute(
                """
            CREATE TABLE Produtor (
            IdProdutor INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(255) NOT NULL,
            IdRegiao INT,
            Telefone VARCHAR(20),
            Website VARCHAR(255),
            Email VARCHAR(255),
            FOREIGN KEY (IdRegiao) REFERENCES Regiao(IdRegiao)
            );"""
            )
            self.connection.commit()
            return (True, None)
        except Exception as error:
            return (False, str(error))

    def CriarTabelaCasta(self):
        try:
            c = self.cursor.execute(
                """
            CREATE TABLE Casta (
            IdCasta INT AUTO_INCREMENT PRIMARY KEY,
            Casta VARCHAR(255) NOT NULL,
            Descricao TEXT
            ); """
            )
            self.connection.commit()
            return (True, None)
        except Exception as error:
            return (False, str(error))

    def CriarTabelaTipoVinho(self):
        try:
            c = self.cursor.execute(
                """
            CREATE TABLE TipoVinho (
            IdTipoVinho INT AUTO_INCREMENT PRIMARY KEY,
            TipoVinho VARCHAR(255) NOT NULL,
            Descricao TEXT 
            ); """
            )
            self.connection.commit()
            return (True, None)
        except Exception as error:
            return (False, str(error))

    def CriarTabelaVinho(self):
        try:
            c = self.cursor.execute(
                """
            CREATE TABLE Vinho (
            IdVinho INT AUTO_INCREMENT PRIMARY KEY,
            Nome VARCHAR(255) NOT NULL,
            Ano YEAR NOT NULL,
            IdProdutor INT NOT NULL,
            IdRegiao INT NOT NULL,
            IdTipoVinho INT NOT NULL,
            Preco DECIMAL(10, 2) NOT NULL,
            Quantidade INT NOT NULL,
            FOREIGN KEY (IdProdutor) REFERENCES Produtor(IdProdutor) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (IdRegiao) REFERENCES Regiao(IdRegiao) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (IdTipoVinho) REFERENCES TipoVinho(IdTipoVinho) ON DELETE CASCADE ON UPDATE CASCADE
            ); """
            )
            self.connection.commit()
            return (True, None)
        except Exception as error:
            return (False, str(error))

    def CriarTabelaVinhoCasta(self):
        try:
            c = self.cursor.execute(
                """
            CREATE TABLE VinhoCasta (
            IdVinhoCasta INT AUTO_INCREMENT PRIMARY KEY,
            IdVinho INT NOT NULL,
            IdCasta INT NOT NULL,
            FOREIGN KEY (IdVinho) REFERENCES Vinho(IdVinho) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (IdCasta) REFERENCES Casta(IdCasta) ON DELETE CASCADE ON UPDATE CASCADE
            ); """
            )
            self.connection.commit()
            return (True, None)
        except Exception as error:
            return (False, str(error))

