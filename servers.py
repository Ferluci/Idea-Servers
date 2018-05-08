import re
import demjson
import requests

def get_servers():
    base_url = 'http://xidea.online/'
    response = requests.get(base_url + 'servers.html')
    servers_file = re.findall(r'assets/js/main-\w*', response.text)[0] + '.js'
    servers_file =requests.get(base_url + servers_file).text

    servers_array_start_index = servers_file.index('servers:')
    start_index = servers_array_start_index + len('servers:')
    end_index = servers_file[servers_array_start_index:].index(']') + servers_array_start_index + 1
    servers_file = servers_file[start_index: end_index]

    return demjson.decode(servers_file)

def print_servers():
    for server in get_servers():
        print(server['url'])

if __name__ == '__main__':
    print_servers()
