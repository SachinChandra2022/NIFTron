from technical_indicators import add_moving_averages, add_rsi, add_macd
from momentum_features import add_price_momentum, add_obv
from featureEngineering.mean_reversion_features import add_price_to_volume_ratio
from utils import fill_missing, clean_stock_data, add_technical_indicators

def apply_all_features(df):
    df = clean_stock_data(df)
    df=add_technical_indicators(df)
    df = add_moving_averages(df)
    df = add_rsi(df)
    df = add_macd(df)
    df = add_price_momentum(df)
    df = add_obv(df)
    df = add_price_to_volume_ratio(df)
    df = fill_missing(df)
    return df