import random

pokeneas = [
    {
        "id": 1,
        "nombre": "Cumbializard",
        "altura": "1.2m",
        "habilidad": "Rumba Fiery",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Cumbializard-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "La vida es una cumbia, hay que bailarla con sabor."
    },
    {
        "id": 2,
        "nombre": "Areparrot",
        "altura": "0.8m",
        "habilidad": "Vuelo Arepero",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/areparrot-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "Con una arepa en la mano, el mundo es más bacano."
    },
    {
        "id": 3,
        "nombre": "Guaroche",
        "altura": "1.5m",
        "habilidad": "Fuerza Llanera",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Guaroche-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "La vida es una batalla, lucha con bravura y verraquera."
    },
    {
        "id": 4,
        "nombre": "Sancocharmeleon",
        "altura": "1.3m",
        "habilidad": "Caldo Revitalizante",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Sancocharmeleon-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "Un buen sancocho cura hasta el alma."
    },
    {
        "id": 5,
        "nombre": "Fritopuff",
        "altura": "0.6m",
        "habilidad": "Explosión Frita",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Fritopuff-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "La vida sin fritanga es como un día sin sol."
    },
    {
        "id": 6,
        "nombre": "Chicharock",
        "altura": "1.4m",
        "habilidad": "Golpe Chicharrón",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/chicharock-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "El chicharrón es el manjar de los valientes."
    },
    {
        "id": 7,
        "nombre": "Patacondor",
        "altura": "1.0m",
        "habilidad": "Ala Crujiente",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Patacondor-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "El que no arriesga no gana, y el que no prueba patacón se lo pierde."
    },
    {
        "id": 8,
        "nombre": "Pandeyuca",
        "altura": "0.5m",
        "habilidad": "Moldeo Flexi",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Pandeyuca-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "La vida es como el pandeyuca, siempre sorprendente."
    },
    {
        "id": 9,
        "nombre": "Cafecachu",
        "altura": "0.9m",
        "habilidad": "Despertar Aroma",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/cafecachu-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "Con un buen café, no hay tristeza que dure."
    },
    {
        "id": 10,
        "nombre": "Buñuelix",
        "altura": "0.7m",
        "habilidad": "Rueda Dulce",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/buuelix-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "La vida es un buñuelo, disfrútala mientras esté calientico."
    },
{
        "id": 11,
        "nombre": "Bandejapaisano",
        "altura": "2.0m",
        "habilidad": "Devastación de calorías",
        "imagen": "https://storage.googleapis.com/pokeneas_alt/Bandejapaijoso-ezgif.com-webp-to-jpg-converter.jpg",
        "frase_filosofica": "Desde el arroz hasta el chorizo, pasando por la arepa y el frijol, hasta la última miga es un himno a la deliciosa pereza."
    }
]

def get_random_pokenea():
    pokenea_index = random.randint(0, 10)
    return pokeneas[pokenea_index]

def get_random_pokenea_subset_1():
    pokenea = get_random_pokenea()
    pokenea_representation = {'nombre': pokenea.get('nombre'), 'altura': pokenea.get('altura'), 'habilidad': pokenea.get('habilidad')}
    return pokenea_representation

def get_random_pokenea_subset_2():
    pokenea = get_random_pokenea()
    pokenea_representation = {'imagen': pokenea.get('imagen'), 'frase': pokenea.get('frase_filosofica')}
    return pokenea_representation

