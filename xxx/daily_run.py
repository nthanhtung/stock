import xxx.extract.vn_direct as vd
import xxx.global_var as gv
import xxx.transform.beta as bt
import pandas as pd

vd.get_stock_price_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021)

vd.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021, type = "quarter")

vd.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021, type = "year")

###################

list_date_to_filter = pd.date_range(start= '1995-12-31', end= '2030-12-31', freq='M', name='Date')
list_date_to_filter = list(map(lambda x: x.strftime('%Y-%m-%d'), list_date_to_filter))

x = bt.calculate_beta(['2021-05-25'], 365)
x.to_csv("data/dim/dim_stock_beta.csv")