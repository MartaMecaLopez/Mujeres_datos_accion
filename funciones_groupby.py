def cambiar_calificacion(calificacion):

    if calificacion == "No":
        buena = calificacion.replace("No", "Buena")
        return buena
    
    elif calificacion == "Si":
        Excelente = calificacion.replace("Si", "Excelente")
        return Excelente    
    
    else:
        return "No calificado"