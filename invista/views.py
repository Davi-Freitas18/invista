from django.shortcuts import render
from django.shortcuts import redirect # faz com que o usuário seja redirecionada a página que desejar.
from django.shortcuts import HttpResponse
from .models import Investimento # Importa tabela criada.
from .forms import InvestimentoForm # Importando form criada.
from django.contrib.auth.decorators import login_required # utilizado para restringir acessos no site se não houver login.

def investimentos(request): # Listagem das colunas da tabela Investimentos.
    dados = {
        'dados': Investimento.objects.all() # Aqui ele está pegando a tabela investimento e trazendo todos os dados de cada coluna.
    }
    return render(request,'investimentos/investimentos.html', context=dados)

def detalhe(request,id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento) # pegando chave primária que for selecionada da tabela investimento.
    }
    return render(request,'investimentos/detalhe.html', dados)

@login_required # restringindo essa função somente para usuários logados.
def criar(request): # Adicionando dados nas colunas da tabela Investimentos.
    if request.method == 'POST': # condição diz que se algo tiver que ser adicionado.
        investimento_form = InvestimentoForm(request.POST) # ele pega todas as informações inputadas.
        if investimento_form.is_valid(): #is_valid() - valida se os dados são válidos.
            investimento_form.save() # Salva as informações no banco de dados.
        return redirect('investimentos') # retornando para página com name definido na url.
    
    else: # quando entra na página pela primeira vez o formulario é criado.
        investimento_form = InvestimentoForm() # nomeando variável para receber classe form.
        formulario = {
            'formulario': investimento_form # criando uma chave para instanciar class form criada.
        }
        return render(request,'investimentos/novo_investimento.html',context=formulario)

@login_required 
def editar(request,id_investimento): # Editando dados adicionados nas colunas.
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'GET':
        formulario = InvestimentoForm(instance=investimento) # aqui ele pega os valores salvos no form criado e mostra pela chave primária selecionada.
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario}) # mostra na tela valores já cadastrados.
    # caso requisição seja POST, ou seja usuário faça alterações no formulário.
    else:
        formulario = InvestimentoForm(request.POST, instance=investimento) # abre o formulário para que o usuário faça as alterações.
        if formulario.is_valid(): # verifica se as alterações feitas foram válidas.
            formulario.save()
        return redirect('investimentos')

@login_required
def excluir(request,id_investimento): # Excluido items.
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method == 'POST': # POST - utilizado quando você envia dados através de uma página. Se clicar no buttom type submit.
        investimento.delete() # Apaga os dados captados pela chave primária selecionada do banco de dados.
        return redirect('investimentos')
    return render(request,'investimentos/confirmar_exclusao.html',{'item': investimento})      
    