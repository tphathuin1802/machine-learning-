import pandas as pd
import plotly.express as px
import requests

api_url = "https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-02-10?adjusted=true&sort=asc&apiKey=J4Vm38LfvgV7z5M_WTYZPkBCJgem_jQH"

response = requests.get(api_url)

if response.status_code == 200:

    data = response.json()

    # Kiểm tra và lấy danh sách kết quả (results) từ dữ liệu JSON
    results = data.get("results", [])

    if results:
        # Chuyển đổi dữ liệu JSON thành DataFrame
        df = pd.DataFrame(results)

        # Định dạng lại cột `t` (timestamp) thành định dạng ngày
        df['date'] = pd.to_datetime(df['t'], unit='ms')

        # Hiển thị thông tin DataFrame
        print(df)
    else:
        print("No results found in API response.")
elif response.status_code == 404:
    print("Cannot search the resources.")
else:
    print(f"Error: {response.status_code}")


    #Plot

    