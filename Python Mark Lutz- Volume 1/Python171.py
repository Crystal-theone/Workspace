import sys
def samplePrint(*args,**kargs):
    sep=kargs.get('sep',' ')
    end=kargs.get('end','\n')
    file=kargs.get('file',sys.stdout)
    output=''
    first=True
    for x in args:
        output+=('' if first else sep)+str(x)
        first=False
    output+=end
    file.write(output)
