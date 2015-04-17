class Controller(object):
    @classmethod
    def render_page(cls):
        outlets = {'outlet':
                   {'1': [{'pin': '27',
                           'label': 'UVA Light'},
                          {'pin': '22',
                           'label': 'Filter'}],
                    '2': [{'pin': '5',
                           'label': 'UVB Light'},
                          {'pin': '6',
                           'label': 'Empty'}]
                    }
                   # 'pin': '13',
                   # 'pin': '19',
                   # 'pin': '26',
                   # 'pin': '23',
                   # 'pin': '24'}
                   }
        data = {"title": "Oulet Controls",
                "data": outlets}
        return data
