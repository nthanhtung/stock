import xxx.extract.api_vn_direct as vd
import xxx.global_var as gv
import xxx.transform.beta_x as bt
import xxx.transform.vnindex as vni
import xxx.extract.web_investing as wi
import datetime as dt
import xxx.extract.web_cophieu68 as cp
import xxx.transform.tram_anh as xta
import pandas as pd
from shutil import copyfile

############### get stock price & finance data from vn direct
data_year = 2021
mr = vd.mass_request(data_path = gv.data_path, vn_top_50 = gv.vn_top_50)

mr.get_stock_price_year_range(symbols = gv.vn_top_50, start_y = data_year, end_y = data_year)

mr.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = data_year, end_y = data_year, type = "quarter")

# mr.get_finance_data_year_range(symbols = gv.vn_top_50, start_y = data_year, end_y = data_year, type = "year")

copyfile(gv.data_path + f"data/finance_data_quarter/finance_data_quarter_{data_year}.csv", gv.data_path + f"data/finance_data_year/finance_data_quarter_{data_year}.csv")

############### get vnindex data from cophieu 68

cp.get_cophieu68(un = "thanhtung211995@gmail.com", pw = "BkkWwkaL123")

############### get bond data from vn_investing

vn_investing = wi.web_scapping_vn_investing(driver_path = "C:\\chromedriver_win32\\chromedriver.exe", download_path = "C:\\Users\\tung.nguyen\\Desktop\\0 Project\\stock\\data\\vn_investing", un = "thanhtung211995@gmail.com", pw = "BkkWwkaL123")
d = vn_investing.get_government_bond_data_of_1_country(url = "https://vn.investing.com/rates-bonds/vietnam-10-year-bond-yield-historical-data", download_file_name = "vietnam_government_bond_data_10_years")
d.close()

############### standardize_vn_index_data
vni.standardize_vn_index_data(gv.data_path)

############### calculate beta


today = dt.datetime.now().strftime('%Y-%m-%d')
x = bt.calculate_beta(gv.data_path, [today], 365)
x.to_csv(gv.data_path + f"data/beta/stock_beta_new.csv")

############### calculate ta
calculate_ta = xta.xxx_tram_anh()
calculate_ta.to_csv(gv.vn_top_50, gv.data_path, history=False)
calculate_ta.append_csv_vnindex(data_path= gv.data_path)

# calculate_ta.to_csv(gv.vn_top_50, gv.data_path, history=True)
