import requests
from fastapi import HTTPException
from langchain.agents import Tool


def __fetch_usd_to_cny_rate__(query: str):
    print("############## 调用 __fetch_usd_to_cny_rate__, 输入参数 = " + str(query))
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CNY&apikey' \
          '=4MPL42O77Y97SYJJ '
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        return f"1 USD = {rate:.2f} CNY"
    except requests.RequestException as e:
        raise HTTPException(status_code=503, detail="Service unavailable")
    except ValueError:
        raise HTTPException(status_code=500, detail="Error parsing JSON data")


def load_tool() -> Tool:
    return Tool(
        name="__fetch_usd_to_cny_rate__",
        func=__fetch_usd_to_cny_rate__,
        description='''
            这个工具可以帮助你调用aliphavantage网站的接口，获取实时美元和人民币之间汇率信息。
            '''
    )