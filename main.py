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

            nome = input("Usuário: ").strip()
            senha = input("Senha: ")

            usuario = UsuarioService.autenticar(
                nome,
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
        print("2 - Ver usuário logado")
        print("3 - Logout")
        print("4 - Sair")
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

            usuario = sessao.obter_usuario()

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

        elif opcao == "3":

            sessao.encerrar_sessao()

            print(
                "\nLogout realizado com sucesso!"
            )

        elif opcao == "4":

            print("\nPrograma encerrado!")
            break

        else:

            print("\nOpção inválida!")