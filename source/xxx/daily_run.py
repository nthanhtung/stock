import xxx.extract.api_vn_direct as vd
import xxx.global_var as gv
import xxx.transform.beta_x as bt
import xxx.transform.vnindex as vni
import xxx.extract.web_investing as wi
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

################

##########

y = wi.web_scapping_vn_investing(driver_path = "C:\\chromedriver_win32\\chromedriver.exe", download_path = "C:\\Users\\tung.nguyen\\Desktop\\0 Project\\stock\\data\\vn_investing", un = "thanhtung211995@gmail.com", pw = "BkkWwkaL123")
d = y.get_government_bond_data_of_1_country(url = "https://vn.investing.com/rates-bonds/vietnam-10-year-bond-yield-historical-data", download_file_name = "vietnam_government_bond_data_10_years")

