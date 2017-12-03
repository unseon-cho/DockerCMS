import requests

def _url(path):
    return 'http://104.199.18.3:8080'+path

def get_containers() :
    return requests.get(_url('/containers'))

def get_containers_running() :
    return requests.get(_url('/containers?state=running'))

def get_services():
    return requests.get(_url('/services'))

def get_nodes():
    return requests.get(_url('/nodes'))

def get_images():
    return requests.get(_url('/images'))

def get_container(con_id):
    return requests.get(_url('/containers/{:s}'.format(con_id)))

def get_container_log(con_id):
    return requests.get(_url('containers/{:s}/logs'.format(con_id)))

def delete_containers():
    return requests.delete(_url('/containers'))

def delete_container(con_id):
    return requests.delete(_url('/containers/{:s}'.format(con_id)))

def delete_images():
    return requests.delete(_url('/images'))

def delete_image(i_id):
    return requests.delete(_url('/images/{:s}'.format(i_id)))


if __name__ == "__main__":
    print(get_containers())
    print(get_containers_running())
    print(get_services())
    print(get_nodes())
    print(get_images())
    print(get_container("0cf4b3f313f4"))
    #print(get_container_log("b9babde8c4db"))
    print(delete_containers())
    print(delete_container("0cf4b3f313f4"))
    print(delete_images())
    print(delete_image("9e7424e5dbae"))





