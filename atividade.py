### **1. Threads para Simulação de Concorrência (Com exemplos simples)**

import threading
import time

def imprimir_pares():
    for i in range(0, 10, 2):
        print(f"Pares: {i}")
        time.sleep(0.1)

def imprimir_impares():
    for i in range(1, 10, 2):
        print(f"Ímpares: {i}")
        time.sleep(0.1)

# Criando as threads
thread_par = threading.Thread(target=imprimir_pares)
thread_impar = threading.Thread(target=imprimir_impares)

# Iniciando as threads
thread_par.start()
thread_impar.start()

# Esperando as threads terminarem
thread_par.join()
thread_impar.join()

print("Fim da execução.")


### **2. Time-Slicing Simulado (Usando `yield`)**

import time

def tarefa_1():
    for i in range(5):
        print(f"Tarefa 1: {i}")
        time.sleep(0.2)
        yield  # Pausa a execução e permite que outra tarefa execute

def tarefa_2():
    for i in range(5):
        print(f"Tarefa 2: {i}")
        time.sleep(0.3)
        yield  # Pausa a execução e permite que outra tarefa execute

def scheduler(tarefas):
    while tarefas:
        for tarefa in tarefas:
            try:
                next(tarefa)  # Executa a tarefa até o próximo yield
            except StopIteration:
                tarefas.remove(tarefa)  # Remove a tarefa se ela terminar

# Criando as tarefas
tarefa1 = tarefa_1()
tarefa2 = tarefa_2()

# Executando as tarefas com o scheduler
scheduler([tarefa1, tarefa2])

print("Fim da execução.")

### **3. Multiprocessamento Básico (Processos Paralelos)**

import multiprocessing

def calcular_soma(lista):
    soma = sum(lista)
    print(f"Soma da lista {lista}: {soma}")

# Definindo as listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Criando os processos
processo1 = multiprocessing.Process(target=calcular_soma, args=(lista1,))
processo2 = multiprocessing.Process(target=calcular_soma, args=(lista2,))

# Iniciando os processos
processo1.start()
processo2.start()

# Esperando os processos terminarem
processo1.join()
processo2.join()

print("Fim da execução.")

### **4. Comunicação entre Processos com Filas**

import multiprocessing

def enviar_mensagens(fila):
    for i in range(5):
        mensagem = f"Mensagem {i}"
        fila.put(mensagem)  # Envia a mensagem para a fila
        print(f"Enviado: {mensagem}")

def receber_mensagens(fila):
    for i in range(5):
        mensagem = fila.get()  # Recebe a mensagem da fila
        print(f"Recebido: {mensagem}")

# Criando a fila
fila = multiprocessing.Queue()

# Criando os processos
processo_envia = multiprocessing.Process(target=enviar_mensagens, args=(fila,))
processo_recebe = multiprocessing.Process(target=receber_mensagens, args=(fila,))

# Iniciando os processos
processo_envia.start()
processo_recebe.start()

# Esperando os processos terminarem
processo_envia.join()
processo_recebe.join()

print("Fim da execução.")

### **5. Simulação de Condição de Corrida (Race Condition)**

import threading
import time

contador = 0
num_incrementos = 10000  # Aumente esse valor para ver melhor a condição de corrida

def incrementar_contador():
    global contador
    for i in range(num_incrementos):
        contador += 1
        if i % 1000 == 0:  # Imprime valores intermediários
            print(f"Thread {threading.current_thread().name}, contador: {contador}")
        time.sleep(0.00001)

# Criando as threads
thread1 = threading.Thread(target=incrementar_contador, name="Thread 1")
thread2 = threading.Thread(target=incrementar_contador, name="Thread 2")

# Iniciando as threads
thread1.start()
thread2.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()

print(f"Valor final do contador: {contador}")

