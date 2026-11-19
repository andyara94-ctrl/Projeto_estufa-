from models.sessao import Sessao
from services.usuario_service import UsuarioService
from services.sensor_service import SensorService

sessao = Sessao()

while True:

    # MENU SEM LOGIN
    if not sessao.usuario_autenticado():

        print("\n========== MENU ==========")
        print("1 - Cadastrar usuário")
        print("2 - Login")
        print("3 - Sair")
        print("==========================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            nome = input("Nome: ").strip()
            email = input("Email: ").strip()
            senha = input("Senha: ")

            UsuarioService.cadastrar(
                nome,
                email,
                senha
            )

        elif opcao == "2":
            
            email = input("E-mail: ")
            senha = input("Senha: ")

            usuario = UsuarioService.autenticar(
                email,
                senha
            )

            if usuario:

                sessao.iniciar_sessao(usuario)

                print(
                    f"\nBem-vindo(a), "
                    f"{usuario.nome}!"
                )

            else:

                print(
                    "\nUsuário ou senha incorretos!"
                )

        elif opcao == "3":

            print("\nPrograma encerrado!")
            break

        else:

            print("\nOpção inválida!")

    # MENU COM LOGIN
    else:

        usuario = sessao.obter_usuario()

        print("\n===== MENU DO USUÁRIO =====")
        print(f"Logado: {usuario.nome}")
        print("1 - Cadastrar sensor")
        print("2 - Ver sensores cadastrados")
        print("3 - Alterar sensor")
        print("4 - Excluir sensor")
        print("5 - Ver usuário logado")
        print("6 - Logout")
        print("7 - Sair")
        print("===========================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":

            while True:

                tipo = input("Tipo: ").strip()

                if tipo:
                    break

                print("Tipo obrigatório!")

            while True:

                descricao = input(
                    "Descrição: "
                ).strip()

                if descricao:
                    break

                print("Descrição obrigatória!")

            while True:

                unidade = input(
                    "Unidade de medida: "
                ).strip()

                if unidade:
                    break

                print(
                    "Unidade obrigatória!"
                )

            SensorService.cadastrar(
                sessao,
                tipo,
                descricao,
                unidade
            )

        elif opcao == "2":

            sensores = SensorService.listar_por_usuario(
                usuario.idusuario
            )

            if not sensores:

                print(
                    "\nNenhum sensor cadastrado."
                )

            else:

                print(
                    "\n===== SENSORES CADASTRADOS ====="
                )

                for sensor in sensores:

                    print(
                        f"\nID do Sensor: {sensor['idsensor']}"
                    )
                    print(
                        f"ID do Usuário: {sensor['id_usuario_cadastro']}"
                    )
                    print(
                        f"Tipo: {sensor['tipo']}"
                    )
                    print(
                        f"Descrição: {sensor['descricao']}"
                    )
                    print(
                        f"Unidade de Medida: {sensor['unidade_medida']}"
                    )
                    print("-" * 40)

        elif opcao == "3":

            idsensor = int(
                input("ID do sensor: ")
            )

            tipo = input(
                "Novo tipo: "
            ).strip()

            descricao = input(
                "Nova descrição: "
            ).strip()

            unidade = input(
                "Nova unidade: "
            ).strip()

            SensorService.alterar(
                idsensor,
                tipo,
                descricao,
                unidade
            )

            print(
                "\nSensor alterado com sucesso!"
            )

        elif opcao == "4":

            idsensor = int(
                input(
                    "ID do sensor a excluir: "
                )
            )

            SensorService.excluir(
                idsensor
            )

            print(
                "\nSensor excluído com sucesso!"
            )

        elif opcao == "5":

            print("\n===== USUÁRIO =====")
            print(
                f"ID: {usuario.idusuario}"
            )
            print(
                f"Nome: {usuario.nome}"
            )
            print(
                f"Email: {usuario.email}"
            )
            print("===================")

        elif opcao == "6":

            sessao.encerrar_sessao()

            print(
                "\nLogout realizado com sucesso!"
            )

        elif opcao == "7":

            print("\nPrograma encerrado!")
            break

        else:

            print("\nOpção inválida!")