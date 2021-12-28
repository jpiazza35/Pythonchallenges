def reloj(*args):
    lista = list(args)
    count = len(lista)
    if(count == 1):
        seconds = args[0]
        minutes = seconds // 60
        segundos_restantes = seconds % 60
        hours = minutes  // 60 
        minutos_restantes = minutes % 60
        print(f'it is {segundos_restantes} seconds, {minutos_restantes} minutes and {hours} hours')
        return hours, minutos_restantes, segundos_restantes

    elif(count == 3):
        hours = args[0]
        minutes = args[1]
        seconds = args[2]
        result_in_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
        print("el tiempo pasado en segundos es: {} ".format(result_in_seconds))
        return result_in_seconds
        





valor = reloj(1200)


