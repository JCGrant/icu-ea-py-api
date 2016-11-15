import requests

class ICUEActivitiesAPI:

    end_point = 'https://eactivities.union.ic.ac.uk/API'

    paths = {
        'list_csp':                     '/CSP',
        'csp_details':                  '/CSP/{code}',

        'list_all_products':            '/CSP/{code}/Products',
        'product_details':              '/CSP/{code}/Products/{id}',
        'product_sales':                '/CSP/{code}/Products/{id}/Sales',

        'profile_entry':                '/CSP/{code}/ProfileEntry',

        'list_purchase_orders':         '/CSP/{code}/PurchaseOrders',
        'purchase_order_details':       '/CSP/{code}/PurchaseOrders/{id}',

        'list_committee':               '/CSP/{code}/Reports/Committee?year={year}',
        'list_members':                 '/CSP/{code}/Reports/Members?year={year}',
        'list_online_sales':            '/CSP/{code}/Reports/OnlineSales?year={year}',
        'list_products':                '/CSP/{code}/Reports/Products?year={year}',
        'list_transaction_lines':       '/CSP/{code}/Reports/TransactionLines?year={year}',

        'list_signups':                 '/CSP/{code}/Signups',
        'signup_details':               '/CSP/{code}/Signups/{id}',

        'list_whatson':                 '/CSP/{code}/WhatsOn',
        'whatson_details':              '/CSP/{code}/WhatsOn/{id}',

        'list_years':                   '/CSP/{code}/Years',
    }

    def __init__(self, csp_code, api_key, year):
        self.csp_code = csp_code
        self.headers = {
            'X-API-Key': api_key,
        }
        self.year = year
        self.__setup_functions()

    def __setup_functions(self):
        for function_name in self.paths.keys():
            self.__setattr__(function_name, self.__create_function(function_name))

    def __get(self, path):
        return requests.get(self.end_point + path, headers=self.headers)

    def __get_json(self, path):
        return self.__get(path).json()

    def __create_function(self, function_name):
        def __call_function(*args, **kwargs):
            path_format = self.paths[function_name]
            year = kwargs.get('year') or self.year
            path = path_format.format(code=self.csp_code, year=year, **kwargs)
            return self.__get_json(path)
        return __call_function
