from django.forms import ModelForm # importando model form para criação de formulários.
from .models import Investimento # Importar todas as tabelas existentes. 

class InvestimentoForm(ModelForm): # Modelo de criação de um form para a tabela investimentos.
    class Meta: # formatação de um form
        model = Investimento # Tabela utilizada
        fields = '__all__' # isso faz com que todos os campos sejam exibidos. se quiser escolher colocar separadamente em uma lista quais campos quer que sejam mostrados.
        

