import Usuario

def main():
    us = Usuario.Usuario()
    us.setNome("Paulo")
    print(us.getNome())
    us.setCPF("703.506.464.81")
    print(us.getCPF())

main()