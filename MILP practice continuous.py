from gekko import GEKKO
m=GEKKO(remote=False) # Initialize gekko
paper_width=8.5
paper_length=11
x=m.Var(lb=0) 

box_width=m.Intermediate(paper_width -2 * x)
box_length=m.Intermediate(paper_length -2 * x)
box_height=m.Intermediate(x)

volume=m.Intermediate(box_width * box_length * box_height)
m.Equation(box_width >= 0)
m.Equation(box_length >= 0)
m.Equation(box_height >= 0)

m.Maximize(volume) 
m.options.SOLVER=1
m.solve(disp=False)

print('Optimal height: ' + str(box_height.value[0]) + ' inches')
print('Optimal width: ' + str(box_width.value[0]) + ' inches')
print('Optimal length: ' + str(box_length.value[0]) + ' inches')
print('Maximum volume: ' + str(volume.value[0]) + ' cubic inches')