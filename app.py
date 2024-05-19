import os

from flask import Flask
from module.pokenea_provider import get_random_pokenea_subset_1, get_random_pokenea_subset_2

app = Flask(__name__)

docker_id = ""

@app.route('/pokenea_subset_1')
def random_pokenea():
    pokenea_information = get_random_pokenea_subset_1()
    pokenea_information['id_contenedor'] = docker_id
    return get_random_pokenea_subset_1()

@app.route('/pokenea_subset_2')
def random_pokenea_representation():
    pokenea_information = get_random_pokenea_subset_2()
    pokenea_information['id_contenedor'] = docker_id
    return get_random_pokenea_subset_1()


if __name__ == '__main__':
    app.run()
