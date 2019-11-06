class Usuario(object):

    def __init__(self):
        self.nome = str
        self.cpf = str
        self.login = str
        self.senha = str
        self.email = str
        self.endereco = str

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setCPF(self, cpf):
        self.cpf = cpf

    def getCPF(self):
        return self.cpf

    def setLogin(self, login):
        self.login = login

    def getLogin(self):
        return self.login

    def setSenha(self, senha):
        self.senha = senha

    def getSenha(self):
        return self.senha

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setEndereco(self, endereco):
        self.endereco = endereco

    def getEndereco(self):
        return self.endereco