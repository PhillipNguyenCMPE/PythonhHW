def cacti_number(plot):
    total = 0
    cacti = 0
    for i in plot:
        for j in i:
            total = total + 1
    row=int(total/len(plot))
    
    for x in range(len(plot)):
        if(len(plot)) == 1:
            cacti = cacti + 1
            break
        for y in range(row):
            if plot[x][y] == 0:
                if (x == 0):
                    if (y == 0):
                        if (plot[x+1][y]) == 0 and (plot[x][y+1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                    elif (y==row-1):
                        if (plot[x+1][y]) == 0 and (plot[x][y-1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                    else:
                        if (plot[x+1][y]) == 0 and (plot[x][y-1] == 0) and (plot[x][y+1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                if (x == len(plot)-1):
                    if (y == 0):
                        if(plot[x-1][y] == 0) and (plot[x][y+1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                    elif (y == row-1):
                        if (plot[x-1][y]) == 0 and (plot[x][y-1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                    else:
                        if (plot[x-1][y] == 0) and (plot[x][y+1] == 0) and (plot[x][y-1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                if (x > 0) and (x < len(plot)-1):
                    if y == 0:
                        if (plot[x+1][y] == 0) and (plot[x-1][y] == 0) and (plot[x][y+1] == 0):
                            plot[x][y] = 1
                            cacti = cacti + 1
                    elif (y == row-1):
                        if ((plot[x+1][y] == 0) and (plot[x-1][y] == 0) and (plot[x][y-1] == 0)):
                            plot[x][y] = 1
                            cacti = cacti + 1
                    else:
                        if ((plot[x+1][y] == 0) and (plot[x-1][y] == 0) and (plot[x][y+1] == 0) and (plot[x][y-1] == 0)):
                            plot[x][y] = 1
                            cacti = cacti + 1
    return cacti
