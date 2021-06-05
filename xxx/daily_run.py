import xxx.get_data as gd
import xxx.global_var as gv

gd.get_stock_price_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021)

gd.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = 2005, end_y = 2021, type = "quarter")

gd.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = 2005, end_y = 2020, type = "year")
