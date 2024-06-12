def render_estudiante_list(estudiantes):
    return [
        {
            "nombre":estudiante.nombre,
            "edad":estudiante.edad,
            "peso":estudiante.peso,
            "bueno":estudiante.bueno,
        }
        for estudiante in estudiantes
    ]
    
def render_estudiante_detail(estudiante):
    return {
            "nombre":estudiante.nombre,
            "edad":estudiante.edad,
            "peso":estudiante.peso,
            "bueno":estudiante.bueno,
        }
