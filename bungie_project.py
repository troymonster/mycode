#!/usr/bin/env python3

import requests
api= "https://www.bungie.net/Platform"
page= "?"
pageSize= "?"
path= "/Forum/GetTopicsPaged/{page}/{pageSize}/{group}/{sort}/{quickDate}/{categoryFilter}/"
resp= requests.get(api + path, auth="API_KEY")
# check the Response box to see what you should get back as a response

