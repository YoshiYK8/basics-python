import random

def fnHola():
    print("Hola")

def fnDado():
    print(random.randint(1,6))

def fnEZPZ():
    print("Too EZ B)")

fnHola()
fnDado()
fnEZPZ()

def hello_world():
    print("Hello World")

def hello_world_name(first_name):
    print (f"Hello, {first_name}")

def hello_world_args(*args):
    first_name = args[0]
    second_name = args[1]
    third_name = args[2]

    print(f"Hello , {first_name} / {second_name} / {third_name} !")
    print(args)
    print(type(args)) #Para saber si args es tupla o algo mas
    print(first_name)

def hello_world_keyword_args(first_person, second_person):
    print(f"Hello , {first_person} / {second_person} !")

def hello_world_arbitrary_keyword_args(**kwargs):
    if kwargs.get['second_person'] is None :
        print("No hay segunda persona")
    else:
        print(kwargs)
        print(type(kwargs))
        print(f"Hello, {kwargs['first_person'] / {kwargs['second_person']}} !")

#hello_world()
#hello_world_name("Yoshio")
#hello_world_args("Sebastian", "Daniel", "Vannessa")
#hello_world_keyword_args(first_person= "Aaron", second_person= "Carla")
#hello_world_arbitrary_keyword_args(first_person= "Bryan", second_person="Cesar")
#hello_world_arbitrary_keyword_args(first_person= "Daniel")
