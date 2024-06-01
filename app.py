from flask import Flask

from module.id_container_provider import read_container_id_from_file
from module.pokenea_provider import get_random_pokenea_subset_1, get_random_pokenea_subset_2

app = Flask(__name__)



docker_id = read_container_id_from_file()

@app.route('/pokenea_subset_1')
def random_pokenea():
    pokenea_information = get_random_pokenea_subset_1()
    pokenea_information['id_contenedor'] = docker_id
    return pokenea_information

@app.route('/pokenea_subset_2')
def random_pokenea_representation():
    pokenea_information = get_random_pokenea_subset_2()
    pokenea_information['id_contenedor'] = docker_id
    return pokenea_information


if __name__ == '__main__':
    app.run()