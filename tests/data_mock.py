import pandas as pd

def pandas_dataframe():
    df = pd.read_html('http://www.ipeadata.gov.br/ExibeSerie.aspx?module=m&serid=1650971490&oper=view', decimal=',', thousands='.', parse_dates=True)[2][1:]
    df.columns=['Date','Preco']
    df.Date = pd.to_datetime(df.Date, dayfirst=True)
    return df