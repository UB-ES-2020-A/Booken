# file deepcode ignore C0411: shut it deepcode
from models.accounts import AccountModel
from models.log import LogModel
from models.orders import OrdersModel
from calendar import monthrange
from datetime import datetime


class DataRetriever:

    @classmethod
    def get_data(cls, needed_data):
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
        elif needed_data == "total_users":
            data = cls._total_users(cls)
        elif needed_data == "log_month":
            data = cls._log_month(cls)
        elif needed_data == "all":
            data = cls._get_all_data(cls)

        return data

    def _get_all_data(self):
        return {'years_data': self._years_data(self),
                'total_sales': self._total_sales(self)['sales'],
                'total_users': self._total_users(self),
                'sales_month': self._sales_month(self),
                'sales_year': self._sales_year(self),
                'sales_genre': self._sales_genre(self),
                'total_gain': self._total_gain(self)['gain'],
                'gain_month': self._gain_month(self),
                'gain_year': self._gain_year(self),
                'gain_genre': self._gain_genre(self),
                'log_month': self._log_month(self)}

    def _years_data(self):
        return sorted({int(o['date'][6:10]) for o in self._get_orders(self)}, reverse=True)

    def _log_month(self):
        year, month, day = datetime.now().year, datetime.now().month, datetime.now().day
        _, ndays = monthrange(year, month)
        logs = {day: 0 for day in range(1, day + 1)}
        for i in LogModel.find_by_month_year(year, month):
            logs[i.day] += 1
        return logs

    def _total_users(self):
        return len([user for user in AccountModel.get_users()['users'] if user['type'] == 0])

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
        years = sorted({int(o['date'][6:10]) for o in orders}, reverse=True)
        n_sales_month = {year: {i: 0 for i in range(1, 13)} for year in years}
        for order in orders:
            year = int(order['date'][6:10])
            month = int(order['date'][3:5])
            for article in order['articles']:
                try:
                    n_sales_month[year][month] += int(article['quant'])
                except KeyError:
                    n_sales_month[month] = int(article['quant'])

        return n_sales_month

    def _gain_month(self):
        orders = self._get_orders(self)
        years = sorted({int(o['date'][6:10]) for o in orders}, reverse=True)
        gain_month = {year: {i: 0 for i in range(1, 13)} for year in years}

        for order in orders:
            year = int(order['date'][6:10])
            month = int(order['date'][3:5])
            try:
                gain_month[year][month] += round(order['total'], 2)
            except KeyError:
                gain_month[year][month] += round(order['total'], 2)
            gain_month[year][month] = round(gain_month[year][month], 2)
        return gain_month

    def _sales_year(self):
        orders = self._get_orders(self)
        years = sorted({int(o['date'][6:10]) for o in orders}, reverse=True)
        n_sales_year = {year: 0 for year in years}
        for order in orders:
            year = int(order['date'][6:10])
            for article in order['articles']:
                try:
                    n_sales_year[year] += int(article['quant'])
                except KeyError:
                    n_sales_year[year] = int(article['quant'])

        return n_sales_year

    def _sales_genre(self):
        orders = self._get_orders(self)
        genres = ['HUMANIDADES', 'TECNICO Y FORMACION', 'METODOS DE IDIOMAS', 'LITERATURA', 'INFANTIL',
                  'COMICS Y MANGA',
                  'JUVENIL', 'OTRAS CATEGORIAS']
        years = sorted({int(o['date'][6:10]) for o in orders}, reverse=True)
        n_sales_genre = {year: {genre: 0 for genre in genres} for year in years}

        for order in orders:
            year = int(order['date'][6:10])
            for article in order['articles']:
                genre = article['categoria']
                try:
                    n_sales_genre[year][genre] += article['quant']
                except KeyError:
                    n_sales_genre[year][genre] = article['quant']

        return n_sales_genre

    def _total_gain(self):
        orders = self._get_orders(self)
        total_gain = 0

        for order in orders:
            total_gain += order['total']

        return {'gain': round(total_gain, 2)}

    def _gain_year(self):
        orders = self._get_orders(self)
        years = sorted({int(o['date'][6:10]) for o in orders}, reverse=True)
        gain_year = {year: 0 for year in years}

        for order in orders:
            year = int(order['date'][6:10])
            try:
                gain_year[year] += round(order['total'], 2)
            except KeyError:
                gain_year[year] = round(order['total'], 2)
            gain_year[year] = round(gain_year[year], 2)
        return gain_year

    def _gain_genre(self):
        orders = self._get_orders(self)
        years = sorted({int(o['date'][6:10]) for o in orders}, reverse=True)
        genres = ['HUMANIDADES', 'TECNICO Y FORMACION', 'METODOS DE IDIOMAS', 'LITERATURA', 'INFANTIL',
                  'COMICS Y MANGA',
                  'JUVENIL', 'OTRAS CATEGORIAS']
        gain_genre = {year: {genre: 0 for genre in genres} for year in years}

        for order in orders:
            year = int(order['date'][6:10])
            for article in order['articles']:
                genre = article['categoria']
                try:
                    gain_genre[year][genre] += round(float(article['price']), 2)
                except KeyError:
                    gain_genre[year][genre] = round(float(article['price']), 2)
            gain_genre[year][genre] = round(gain_genre[year][genre], 2)
        return gain_genre
