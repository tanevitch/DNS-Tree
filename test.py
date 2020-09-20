from anytree import Node, RenderTree
from anytree.exporter import DotExporter

#root= Node("root", children= [ Node("com", children= [ Node("google")]), Node("edu"), Node("gob"), Node("mil"), Node("org"), Node("net"), Node("int") ])   

root = Node("root") 

def doesnt_exist(dom_node, dom, length):
    if (length>=0):
        print("<",dom_node.name,"> will delegate a new domine..")
        print(dom[length]," domain name will be created. Accept? Y/n")
        opt = input()
        print()
        if (opt.upper() == "Y"):
            new= Node(dom[length])
            l = list(dom_node.children)
            l.append(new)
            dom_node.children = l
            doesnt_exist(new, dom, length-1)
        else:
            print('///  Operation cancelled')
            print()
            return

def search_domine(dom, length, dom_node):
    ok= False
    if (length >= 0):
        for child in dom_node.children:
            if (child.name == dom[length]):
                search_domine(dom, length-1, child)
                ok= True    
                break
        if (not ok):
            print("<",dom_node.name,"> will delegate a new domine..")
            print(dom[length]," domain name will be created. Accept? Y/n")
            opt = input()
            print()
            if (opt.upper() == "Y"):
                new= Node(dom[length])
                l = list(dom_node.children)
                l.append(new)
                dom_node.children = l
                doesnt_exist(new, dom, length-1)
            else:
                print('///  Operation cancelled')
                print()
                return

def create_node(parsed_dom):
    length = len(parsed_dom)-1
 
    if (search_in_tree(parsed_dom, length, root) == None):
        print()
        print("Add <",parsed_dom[length], "> as new TLD name? Y/n")
        opt = input()
        print()
        if (str(opt).upper() == "Y"):
            new= Node(parsed_dom[length])
            l = list(root.children)
            l.append(new)
            root.children = l
            doesnt_exist(new, parsed_dom, length-1)
        else:
            print("///  Operation cancelled")
            print()
    else:      
        search_domine(parsed_dom, length, root)

    '''length = len(parsed_dom)-1
    search_domine(parsed_dom, length, root)'''

def create_from_txt():
    file = open("input.txt", "r")
    for each in file:
        prev= each.split('\n')
        parsed_dom = prev[0].split(".")
        create_node(parsed_dom)

def search_in_tree(dom, length, node):
    if (length>=0):
        for child in node.children:
            if (child.name == dom[length]):
                search_in_tree(dom, length, child)
                return child


def menu():
    print('Enter 1 for create a DNS tree from .txt')
    print('Enter 2 for add a node (domain name)')
    print('Enter 3 for search a domain name in the DNS tree')
    opt = input("Your selection: ")
    if (int(opt) == 1): 
        create_from_txt()
    else:
        if (int(opt) == 2):
            dom= input("Insert the domain name for create a new node // Ex: 'mail.google.com' --> ")
            parsed_dom = dom.split(".") 
            if (parsed_dom[0] == ""):
                parsed_dom.remove("")
            create_node(parsed_dom)
        else:
            if (int(opt) == 3):
                dom = input("Insert the domain name for search // Ex: 'google.com' --> ")
                parsed_dom = dom.split(".")
                print(search_in_tree(parsed_dom, len(parsed_dom)-1, root))
            else:
                print("EXIT")

#------------------------------------------------------------------------------------------------------------
print(' Welcome!')
print('-----------------------------------')
ok = True
while (ok):   
    menu()
    opt = input("Continue..? Y/n ")
    if (opt.upper() == "N"):
        ok= False
#------------------------------------------------------------------------------------------------------------


print('-----------------------------------')
print('OUTPUT DNS TREE')
for pre, fill, node in RenderTree(root):
    print("%s%s" % (pre, node.name))

DotExporter(root).to_picture("udo.png")

#Casos base: Si agregás un dominio, te va a pedir permiso para crear el TLD