import yfinance as yf
from plotnine import *

data = yf.download("BBAS3.SA")

ggplot(
    data = data.reset_index(),
    mapping = aes(x = "Date", y = "Close")
) +\
    geom_line() +\
    ggtitle("Dados históricos do BBAS3") +\
    xlab('Data') +\
    ylab('Fechamento')



##################################

from data.download import download_data