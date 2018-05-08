import re
import demjson
import requests

base_url = 'http://xidea.online/'
response = requests.get(base_url + 'servers.html')
servers_file = re.findall(r'assets/js/main-\w*', response.text)[0] + '.js'
servers_file =requests.get(base_url + servers_file).text

servers_array_start_index = servers_file.index('servers:')
start_index = servers_array_start_index + len('servers:')
end_index = servers_file[servers_array_start_index:].index(']') + servers_array_start_index + 1
servers_file = servers_file[start_index: end_index]

servers = demjson.decode(servers_file)
for server in servers:
    print(server['url'])
