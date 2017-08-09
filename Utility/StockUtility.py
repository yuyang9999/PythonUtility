
import pandas_datareader.data as web

class StockUtility:
    @staticmethod
    def download_stock_data(symbol_name, start_time, end_time = None):
        get_function = [web.get_data_yahoo, web.get_data_enigma, web.get_data_google, web.get_data_famafrench,
                        web.get_data_fred, web.get_data_quandl]
        data = None
        succeed = False
        for func in get_function:
            if not succeed:
                succeed = True
                try:
                    if end_time is None:
                        data = func(symbol_name, start_time)
                    else:
                        data = func(symbol_name, start_time, end_time)
                except Exception as e:
                    succeed = False
            if succeed:
                break
        if not succeed:
            return False, data

        return True, data