def display_grid():
    multiple_grid_genrator(2,2)
    single_grid_genrator(4,3)
    multiple_grid_genrator(2,2)
    single_grid_genrator(4,3)
    multiple_grid_genrator(2,2)
    single_grid_genrator(4,3)
    multiple_grid_genrator(2,2)
    single_grid_genrator(4,3)
    multiple_grid_genrator(2,2)
def multiple_grid_genrator(repeat_count,column_repeat):
    print (('+'+('-'*4))*column_repeat)*repeat_count+"+","\n",
def single_grid_genrator(repeat_count,column_repeat):
    print (('|'+(' '*9))*column_repeat+'\n')*repeat_count,
display_grid()