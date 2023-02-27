from django.shortcuts import render, redirect
from django.contrib import messages # envia mensagems para o usuário tempo a opção de escolha de que tipo de mensagem deseja enviar.
from .forms import UserRegisterForm # Faz com que o cadastro de um novo usuário seja feio automaticamente. Com as alterações feitas na criação desta classe form.


def novo_usuario(request):
    # tipo da requisição, validar, informar, salvar.
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST) # request.POST faz com que as informações do cadastro sejam salvas na variável formulário.
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')

    else:
        formulario = UserRegisterForm()


    return render(request,'usuarios/registrar.html',{'formulario': formulario})