from data.download import download_data
from plotnine import( 
    ggplot, aes,
    geom_line,
    ggtitle,
    xlab, ylab
)

def plot_line(ticker:str) -> ggplot:
    """Flat a static plot using plotline.

    Args:
        ticker (str): The ticker of Financial asset.

    Returns:
        ggplot: A line chart depiciting the historical closing prices.
    """
    

    data = download_data(ticker)

    fig = ggplot(
        data = data.reset_index(),
        mapping = aes(x = "Date", y = "Close")
    ) +\
        geom_line() +\
        ggtitle(f'Dados históricos do {ticker}') +\
        xlab('Data') +\
        ylab('Fechamento')

    return fig