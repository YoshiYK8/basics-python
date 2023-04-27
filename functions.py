
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


#hello_world()
#hello_world_name("Yoshio")
hello_world_args("Sebastian", "Daniel", "Vannessa")