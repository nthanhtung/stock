
---------

use case

stock scan based on signal:
	technical analysis
	fundamental analysis

stock correlation with relevant commodity:
    HPG with steel
    PNJ with gold
    PVS with VNindex

data source
    https://www.cophieu68.vn/export.php
    https://finfoapi-hn.vndirect.com.vn/stocks/adPrice?symbols=HOSE&fromDate=2015-01-01&toDate=2021-05-31
    https://finfo-api.vndirect.com.vn/v3/stocks/financialStatement?secCodes=VNM&fromDate=2017-06-30&toDate=2019-06-30

example template
    https://github.com/wilsonfreitas/awesome-quant
    https://pypi.org/project/finance-calculator/
    https://indzara.com/stock-market-templates/
    https://stackoverflow.com/questions/39501277/efficient-python-pandas-stock-beta-calculation-on-many-dataframes
---------

E
	get data 20 y 1 shot
	get data this y daily
	VN data: higher prority
        firm finance statement
	    price & volume data
        stock symbal mapping: industry
    World data:
        US stock market
        Comodity price


T
	technical analysis
	fundamental analysis
    benchmark analysis:
        industry
        regional, global
	backtest & strategy efficiency analysis
    stock correlation with relevant commodity
	

L
	write semantic layer data to yearly file

-------

design

text
diagram
sttm
report template: excel/power bi/web mockup

------------

market gap in stock trading analysis tool

    stock valuation tool:
        input:
            growth assumption
            market risk
    

    stock scan based on stock valuation


    industry benchmarking tool:
        p/e
        p/b
        beta
        vs us, asean


---------
Discounted cash flow (DCF) valuation views the intrinsic value of a security
    cash flows actually paid to stockholders
        dividend discount model (DDM)
    cash flows available for distribution to shareholders
        free cash flow to the firm (FCFF)
        free cash flow to equity (FCFE)
        analysts consider free cash flow models to be more useful than DDMs in practice
        Free cash flows provide an economically sound basis for valuation
    market multiples

    practice
        residual income
        dividend discount
        discounted free cash flow
        FCFF models are used roughly twice as frequently as FCFE models
        Analysts like to use free cash flow as the return (either FCFF or FCFE)
            The company does not pay dividends.
            Free cash flows align with profitability within a reasonable forecast period with which the analyst is comfortable.




Calculation

FCFF = CFO + Int(1 – Tax rate) – FCInv.

FCFE = CFO – FCInv + Net borrowing.

Equity value = Firm value – Market value of debt.

Dividing the total value of equity by the number of outstanding shares gives the value per share.

----------

WACC  =  (E/V x Re)  +  ((D/V x Rd)  x  (1 – T))

Where:

E = market value of the firm’s equity (market cap)
D = market value of the firm’s debt
V = total value of capital (equity plus debt)
E/V = percentage of capital that is equity
D/V = percentage of capital that is debt
Re = cost of equity (required rate of return)
Rd = cost of debt (yield to maturity on existing debt)
T = tax rate

Re  =  Rf  +  β  ×  (Rm − Rf)

Where:

Rf = the risk-free rate (typically the 10-year U.S. Treasury bond yield)
β = equity beta (levered)
Rm = annual return of the market


