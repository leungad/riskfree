# riskfree
Risk Free Web Scrape Function

The riskfree web scrape function finds a general risk free rate for emerging market companies based upon the country, utilizing a country default spread from NYU's Professor Aswath Damodaran's Research. The Function scrapes the data from his website in the form of a table provided, which it then looks for the 10 Year Government bond yield for the country. 
Lastly, it calculates the risk free rate as a function of (ten_year_yield - adjusted spread)/100 to return the expected risk free rate for the country.
