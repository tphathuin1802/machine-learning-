import plotly.express as px
import plotly.graph_objects as go


import requests # nhập thư viện requests

response = requests.get("API_END_POINT")
if response.status_code == 200:
    data = response.json() # vì api sử dụng json file
    print(data)
    print("Successfully")
elif response.status_code == 404:
    print("Cannot search the resources")
else:
    print(f"Error, {response.status_code}")
