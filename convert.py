with open('main_template.tex') as f:
    lines  = ['"'+ s.strip() + '"' for s in f.readlines()]
    prefix = '\\\\'
    for line in lines :
        line = line.replace('\\', prefix )
        print(line)
    
