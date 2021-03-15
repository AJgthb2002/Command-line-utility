import argparse
import sys
from datetime import date


def get_count(myfile):
    count=0
    for line in myfile: 
        count += 1
    return count    

def print_todos():
    file1=open("todo.txt", 'r')
    lines = file1.read().splitlines()
    for i in reversed(range(len(lines))):
        print("[{}] {}".format(i+1, lines[i].strip()))   

today = date.today()
def print_date():
    d = today.strftime("%Y-%m-%d")
    return str(d)
    #sys.stdout.write(print_date())

def calc(args):
    if args.instruction=="help":
        print('Usage :-\n$ ./todo add "todo item"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics')
   
    elif args.instruction=="add":
        with open("todo.txt", 'a+') as file1:
            add_string="{}{}".format(args.value,"\n")
            file1.write(add_string)
            print('Added todo: "{}"'.format(args.value))
            file1.close()     
    
    elif args.instruction=="done":
        file1=open("todo.txt", 'r')
        if get_count(file1)>= int(args.value):
            print('Marked todo #{} as done.'.format(args.value))
            # del that todo and add it to done
            file1.close()
            file1=open("todo.txt", 'r')
            lines = file1.read().splitlines()
            deleted=lines[int(args.value)-1]
            del lines[int(args.value)-1]
            file1.close()

            file1=open("todo.txt", 'w')
            for line in lines:
                file1.write(line+"\n")
            file1.close()
            file2= open("done.txt", 'a+')
            file2.write("x "+print_date()+" "+deleted+"\n")
            file2.close()

        else:
            print('Error: todo #{} does not exist.' .format(args.value))
            file1.close() 
          

    elif args.instruction=="del":
        file1= open("todo.txt", 'r')
        if get_count(file1)>= int(args.value):
            print('Deleted todo #{}'.format(args.value))
            # del from todo file
            file1.close()
            file1=open("todo.txt", 'r')
            lines = file1.read().splitlines()
            deleted=lines[int(args.value)-1]
            del lines[int(args.value)-1]
            file1.close()

            file1=open("todo.txt", 'w')
            for line in lines:
                file1.write(line)
            file1.close()

        else:
            print('Error: todo #{} does not exist. Nothing deleted.' .format(args.value))
            file1.close()         
    
    elif args.instruction=="ls":
        print_todos() 
    
    elif args.instruction=="report":
        file1=open("todo.txt", 'r')
        file2=open("done.txt", 'r')
        print('{} Pending : {} Completed : {} '.format(print_date(), get_count(file1), get_count(file2)))        
    
    else:
        return "Something went wrong"                 

if __name__=='__main__':
    parser= argparse.ArgumentParser()
    
    parser.add_argument("instruction", nargs="?", default= "help")
    parser.add_argument("value", nargs="?", default= "noval")
    
    args= parser.parse_args()
    calc(args)
     
