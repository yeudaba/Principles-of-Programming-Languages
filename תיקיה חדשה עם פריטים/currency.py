
class currency:
    def make_currency(amount, symbol):

        data = {'amount': amount, 'symbol': symbol}

        def dispatch(message):
            if message == 'get_value':

                def get_value(key):
                    if key == 'amount':
                        return data['amount']
                    elif key == 'symbol':
                        return data['symbol']
                    else:
                        raise ValueError("Invalid key")

                return get_value
            elif message == 'set_value':

                def set_value(key, value):
                    if key == 'amount':
                        data['amount'] = value
                    elif key == 'symbol':
                        data['symbol'] = value
                    else:
                        raise ValueError("Invalid key")

                return set_value
            elif message == 'str':

                return f"{data['symbol']}{data['amount']:.2f}"
            elif message == 'convert':

                def convert(conversion_lambda, new_symbol):
                    data['amount'] = conversion_lambda(data['amount'])
                    data['symbol'] = new_symbol

                return convert
            else:
                raise ValueError("Invalid message")

        return dispatch
