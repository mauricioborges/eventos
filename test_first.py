from eventos import Agenda

# content of test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 5

def test_criar_uma_agenda_com_nome():
# quando eu crio um objeto Agenda, eu preciso passar um nome pra ele
# esse nome vai retornar quando eu perguntar
    agenda = Agenda("um nome")
    assert agenda.nome() == "um nome"
