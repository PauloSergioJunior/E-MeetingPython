import Reuniao

class GerenciaReuniao:

    def __init__(self):
        self.dados = []

    def criarReuniao(self, participantes, local,dataReuniao,ata):
        r = Reuniao.Reuniao
        r.setParticipantes(participantes)
        r.setLocal(local)
        r.setDataReuniao(dataReuniao)
        r.setAta(ata)
        
    def editarAta(self, reuniao,ata):
        """

        :type reuniao: object
        """
        reuniao.setAta(ata)