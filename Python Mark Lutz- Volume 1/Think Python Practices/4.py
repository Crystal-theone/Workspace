def do_twice(f,num):
    f(num)
    f(num)
def print_spam(num):
    print "Hello, I am a spam."+" with a value of "+str(num)
def print_twice(value):
    print value
    print value
def do_four(f,statement):
    f(statement)
    f(statement)
do_four(print_twice,"Sample")