# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (2 ciudades)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # PPUJILI
        [   # Semana 1
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 12},
            {"dia": "Miércoles", "temp": 41},
            {"dia": "Jueves", "temp": 12},
            {"dia": "Viernes", "temp": 14},
            {"dia": "Sábado", "temp": 12},
            {"dia": "Domingo", "temp": 72}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 14},
            {"dia": "Martes", "temp": 35},
            {"dia": "Miércoles", "temp": 42},
            {"dia": "Jueves", "temp": 24},
            {"dia": "Viernes", "temp": 54},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 40}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 15},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 30},
            {"dia": "Jueves", "temp": 52},
            {"dia": "Viernes", "temp": 44},
            {"dia": "Sábado", "temp": 44},
            {"dia": "Domingo", "temp": 25}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 48},
            {"dia": "Martes", "temp": 36},
            {"dia": "Miércoles", "temp": 18},
            {"dia": "Jueves", "temp": 20},
            {"dia": "Viernes", "temp": 35},
            {"dia": "Sábado", "temp": 30},
            {"dia": "Domingo", "temp": 30}
        ]
    ],
    [   # LATACUNGA
        [   # Semana 1
            {"dia": "Lunes", "temp": 25},
            {"dia": "Martes", "temp": 10},
            {"dia": "Miércoles", "temp": 10},
            {"dia": "Jueves", "temp": 15},
            {"dia": "Viernes", "temp": 20},
            {"dia": "Sábado", "temp": 45},
            {"dia": "Domingo", "temp": 30}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 30},
            {"dia": "Martes", "temp": 15},
            {"dia": "Miércoles", "temp": 15},
            {"dia": "Jueves", "temp": 50},
            {"dia": "Viernes", "temp": 70},
            {"dia": "Sábado", "temp": 40},
            {"dia": "Domingo", "temp": 30}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 40},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 25},
            {"dia": "Jueves", "temp": 39},
            {"dia": "Viernes", "temp": 47},
            {"dia": "Sábado", "temp": 25},
            {"dia": "Domingo", "temp": 15}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 40},
            {"dia": "Martes", "temp": 30},
            {"dia": "Miércoles", "temp": 90},
            {"dia": "Jueves", "temp": 80},
            {"dia": "Viernes", "temp": 60},
            {"dia": "Sábado", "temp": 40},
            {"dia": "Domingo", "temp": 20}
        ]
    ],
    [   # QUITO
        [   # Semana 1
            {"dia": "Lunes", "temp": 45},
            {"dia": "Martes", "temp": 65},
            {"dia": "Miércoles", "temp": 70},
            {"dia": "Jueves", "temp": 80},
            {"dia": "Viernes", "temp": 50},
            {"dia": "Sábado", "temp": 40},
            {"dia": "Domingo", "temp": 70}
        ],
        [   # Semana 2
            {"dia": "Lunes", "temp": 20},
            {"dia": "Martes", "temp": 60},
            {"dia": "Miércoles", "temp": 74},
            {"dia": "Jueves", "temp": 80},
            {"dia": "Viernes", "temp": 71},
            {"dia": "Sábado", "temp": 69},
            {"dia": "Domingo", "temp": 58}
        ],
        [   # Semana 3
            {"dia": "Lunes", "temp": 71},
            {"dia": "Martes", "temp": 43},
            {"dia": "Miércoles", "temp": 55},
            {"dia": "Jueves", "temp": 82},
            {"dia": "Viernes", "temp": 85},
            {"dia": "Sábado", "temp": 86},
            {"dia": "Domingo", "temp": 83}
        ],
        [   # Semana 4
            {"dia": "Lunes", "temp": 78},
            {"dia": "Martes", "temp": 40},
            {"dia": "Miércoles", "temp": 62},
            {"dia": "Jueves", "temp": 30},
            {"dia": "Viernes", "temp": 30},
            {"dia": "Sábado", "temp": 13},
            {"dia": "Domingo", "temp": 20}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
ciudades = ["PUJILI", "LATACUNGA", "QUITO"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio:.2f} grados")
