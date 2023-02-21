#!/usr/bin/python3

import requests

url = 'https://www.hawkwheels.be/wp-content/uploads/2022/05/Logo-hawkwheels.png'
r = requests.get(url, allow_redirects=True)
open('hawkwheels.png', 'wb').write(r.content)