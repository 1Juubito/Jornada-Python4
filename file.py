# Título : Hashzap
# Botão iniciar chat
    # Clicou no botão:
        # Popup / Modal
            # Título : Bem vindo ao Hashzap
            # Campo : Escreva seu nome no chat
            # Botão : Entrar no chat
# Chat
# Embaixo do chat
    # Campo de digite sua mensagem
    # Botão de enviar

# Flet ~> Framework do Python
# pip install flet

import flet as ft #importar flet

def main(pagina): #Criar função principal/main
    texto = ft.Text("Hashzap")

    chat = ft.Column()

    def enviar_mensagem_tunel(mensagem):
        # Adicione a mensagem no chat
        texto_mensagem = ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        print("Enviar mensagem")
        pagina.pubsub.send_all(f"{nome_usuario.value}: {campo_mensagem.value}")
        
        # Limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()




    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_mensagem, botao_enviar])
    def entrar_chat(evento):
        print("Entrar no chat")
        #fechar o popup
        popup.open = False
        #tirar botão iniciar chat
        pagina.remove(botao_inciar)
        # tirar o titulo hashzap
        pagina.remove(texto)
        # criar o chat
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_usuario.value} entrou no chat")
        # colocar o campo de digitar mensagem
        pagina.add(linha_enviar)
        # criar botão enviar
        pagina.update()

    
    titulo_popup = ft.Text("Bem vindo ao Hashzap")
    nome_usuario = ft.TextField(label="Escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

    popup = ft.AlertDialog(
        open=False,
        modal=True,
        title=titulo_popup,
        content=nome_usuario,
        actions=[botao_entrar]
    )



    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        # Sempre que editar a página depois que a página tiver carregada, você tem que rodar pagina.update() sempre que fizer edição
        pagina.update()

    

    botao_inciar = ft. ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_inciar)


ft.app(target=main, view=ft.WEB_BROWSER) # Criar o app chamando a função principal

