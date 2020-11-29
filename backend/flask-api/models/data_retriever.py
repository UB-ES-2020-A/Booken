from models.orders import OrdersModel

class DataRetriever():

    @classmethod
    def get_data(cls,needed_data):
        data = None
        
        if needed_data == "total_sales":
            data = cls._total_sales(cls)
        elif needed_data == "sales_month":
            data = cls._sales_month(cls)
        elif needed_data == "sales_year":
            data = cls._sales_year(cls)
        elif needed_data == "sales_genre":
            data = cls._sales_genre(cls)
        elif needed_data == "total_gain":
            data = cls._total_gain(cls)
        elif needed_data == "gain_month":
            data = cls._gain_month(cls)
        elif needed_data == "gain_year":
            data = cls._gain_year(cls)
        elif needed_data == "gain_genre":
            data = cls._gain_genre(cls)
        
        return data

    def _get_orders(self):
        return OrdersModel.get_orders()['orders']

    def _total_sales(self):
        orders = self._get_orders(self)
        n_sales = 0
        for order in orders:
            for article in order['articles']:
                n_sales += int(article['quant'])

        return {'sales': n_sales}

    def _sales_month(self):
        orders = self._get_orders(self)
        n_sales_month = {}

        for order in orders:
            month = order['date'][-7:]
            for article in order['articles']:
                try:
                    n_sales_month[month] += int(article['quant'])
                except KeyError:
                    n_sales_month[month] = int(article['quant'])

        return n_sales_month

    def _sales_year(self):
        orders = self._get_orders(self)
        n_sales_year = {}

        for order in orders:
            year = order['date'][-4:]
            for article in order['articles']:
                try:
                    n_sales_year[year] += int(article['quant'])
                except KeyError:
                    n_sales_year[year] = int(article['quant'])

        return n_sales_year

    def _sales_genre(self):
        orders = self._get_orders(self)
        n_sales_genre = {}

        for order in orders:
            for article in order['articles']:
                genre = article['categoria']
                try:
                    n_sales_genre[genre] += article['quant']
                except KeyError:
                    n_sales_genre[genre] = article['quant']

        return n_sales_genre

    def _total_gain(self):
        orders = self._get_orders(self)
        total_gain = 0

        for order in orders:
            total_gain += order['total']

        return {'gain': total_gain}

    def _gain_month(self):
        orders = self._get_orders(self)

        gain_month = {}

        for order in orders:
            month = order['date'][-7:]
            try:
                gain_month[month] += order['total']
            except KeyError:
                gain_month[month] = order['total']

        return gain_month

    def _gain_year(self):
        orders = self._get_orders(self)

        gain_month = {}

        for order in orders:
            year = order['date'][-4:]
            try:
                gain_month[year] += order['total']
            except KeyError:
                gain_month[year] = order['total']

        return gain_month

    def _gain_genre(self):
        orders = self._get_orders(self)

        gain_genre = {}

        for order in orders:
            for article in order['articles']:
                genre = article['categoria']
                try:
                    gain_genre[genre] += float(article['price'])
                except KeyError:
                    gain_genre[genre] = float(article['price'])

        return gain_genre
