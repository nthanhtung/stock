import xxx.extract.api_vn_direct as vd
import xxx.global_var as gv
import xxx.transform.beta_x as bt
import xxx.transform.vnindex as vni
import datetime as dt


mr = vd.mass_request(data_path = gv.data_path, vn_top_50 = gv.vn_top_50)

mr.get_stock_price_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021)

mr.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021, type = "quarter")

mr.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = 2021, end_y = 2021, type = "year")

###################


today = dt.datetime.now().strftime('%Y-%m-%d')
x = bt.calculate_beta(gv.data_path, [today], 365)
x.to_csv(gv.data_path + "data/dim/dim_stock_beta_1_day.csv")

####################

vni.standardize_vn_index_data(gv.data_path)
vni.xxx()