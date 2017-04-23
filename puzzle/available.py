from operator import itemgetter


def read_line_to_list(as_type=int):
    return map(as_type, raw_input().strip().split(' '))


class BAvailable(object):
    def __init__(self, n_nights, n_prices, info):
        self.n_nights = n_nights
        self.n_prices = n_prices
        self.info = info
        self.min_prices_ = [None] * self.n_nights
        self.construct_min_prices()

    def construct_min_prices(self):
        prices, min_stay, max_stay = self.info

        for i in range(self.n_nights):
            nights = i + 1

            def get_price(p):
                return p[0] if p[0] > 0 and p[1] <= nights <= p[2] else -1

            def reduce_price(p, q):
                return map(
                    lambda x: abs(x[0] * x[1]) if x[0] * x[1] < 0 else min(x),
                    zip(p, q)
                )

            self.min_prices_[i] = reduce(reduce_price, (map(
                get_price, zip(prices[j], min_stay[j], max_stay[j])
            ) for j in range(self.n_prices)))

    def get_total_min_price(self, start, nights):
        min_prices = self.min_prices_[nights - 1][
                     start - 1: start + nights - 1
                     ]
        return -1 if any(p < 0 for p in min_prices) else sum(min_prices)


N, M, Q = read_line_to_list()
INFO = [None] * 3
for i0 in range(3):
    INFO[i0] = [read_line_to_list() for _ in range(M)]

avail = BAvailable(N, M, INFO)

# print avail.get_total_min_price(6, 2)
# print avail.min_price_by_night_
# print avail.get_min_price(0, 1)
for _ in range(Q):
    print avail.get_total_min_price(*read_line_to_list())

# print avail.min_price_by_night_

