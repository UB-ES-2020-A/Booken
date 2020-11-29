from models.orders import OrdersModel

class DataRetriever():

    @classmethod
    def get_data(self,needed_data):
        if needed_data == "total_sales":
            return self.total_sales(self)
        elif needed_data == "sales_month":
            return self.sales_month(self)
        elif needed_data == "sales_year":
            return self.sales_year(self)
        elif needed_data == "sales_genre":
            return self.sales_genre(self)
        elif needed_data == "total_gain":
            return self.total_gain(self)
        elif needed_data == "gain_month":
            return self.gain_month(self)
        elif needed_data == "gain_year":
            return self.gain_year(self)
        elif needed_data == "gain_genre":
            return self.gain_genre(self)
        else:
            return

    def get_orders(self):
        return OrdersModel.get_orders()['orders']

    def total_sales(self):
        orders = self.get_orders(self)
        n_sales = 0
        for order in orders:
            for article in order['articles']:
                n_sales += int(article['quant'])

        return {'sales': n_sales}

    def sales_month(self):
        orders = self.get_orders(self)
        n_sales_month = {}

        for order in orders:
            month = order['date'][-7:]
            for article in order['articles']:
                try:
                    n_sales_month[month] += int(article['quant'])
                except:
                    n_sales_month[month] = int(article['quant'])

        return n_sales_month

    def sales_year(self):
        orders = self.get_orders(self)
        n_sales_year = {}

        for order in orders:
            year = order['date'][-4:]
            for article in order['articles']:
                try:
                    n_sales_year[year] += int(article['quant'])
                except:
                    n_sales_year[year] = int(article['quant'])

        return n_sales_year

    def sales_genre(self):
        orders = self.get_orders(self)
        n_sales_genre = {}

        for order in orders:
            for article in order['articles']:
                genre = article['categoria']
                try:
                    n_sales_genre[genre] += article['quant']
                except:
                    n_sales_genre[genre] = article['quant']

        return n_sales_genre

    def total_gain(self):
        orders = self.get_orders(self)
        total_gain = 0

        for order in orders:
            total_gain += order['total']

        return {'gain': total_gain}

    def gain_month(self):
        orders = self.get_orders(self)

        gain_month = {}

        for order in orders:
            month = order['date'][-7:]
            try:
                gain_month[month] += order['total']
            except:
                gain_month[month] = order['total']

        return gain_month

    def gain_year(self):
        orders = self.get_orders(self)

        gain_month = {}

        for order in orders:
            year = order['date'][-4:]
            try:
                gain_month[year] += order['total']
            except:
                gain_month[year] = order['total']

        return gain_month

    def gain_genre(self):
        orders = self.get_orders(self)

        gain_genre = {}

        for order in orders:
            for article in order['articles']:
                genre = article['categoria']
                try:
                    gain_genre[genre] += float(article['price'])
                except:
                    gain_genre[genre] = float(article['price'])

        return gain_genre
