import Usuario
import GerenciaReuniao
import Reuniao


def main():
    us = Usuario.Usuario()
    us.setNome("Paulo")
    us.setEmail('Junior@gmail.com')
    us.setEndereco('Rua a')
    us.setCPF("703.506.464.81")


    us2 = Usuario.Usuario()
    us2.setNome("Sergio")
    us2.setEmail('Juniorvasco@gmail.com')
    us2.setEndereco('Rua b')
    us2.setCPF("703.506.464.81")

    participant = []
    participant.append(us)
    participant.append(us2)

    r = Reuniao.Reuniao()

    #r.setParticipantes(participant)

    #print(participantes)

    #print(r.getParticipantes())

    gr = GerenciaReuniao.GerenciaReuniao()

    print(gr.criarReuniao(participant,"Local a","14/11/2019","Ata desconhecida"))

    r2 = gr.criarReuniao(participant,"Local a","14/11/2019","Ata desconhecida")

    print(gr.editarAta(r2,'Ata Conhecida'))

main()