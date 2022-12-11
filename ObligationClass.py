class ObligationClass:
    
    def __init__(self, lots, nominal, percent, SCI, cupn_in_one_year, cupn_total):

        self.nominal = nominal 
        self.percent = percent
        self.SCI = SCI
        self.cupn_in_one_year = cupn_in_one_year
        self.cupn_total = cupn_total
        self.lots = lots

    def result_cupn(self):

        self.payment = self.lots * (self.nominal * (self.percent / ((self.cupn_in_one_year * 100))))
        self.first_payment = self.payment - self.lots * self.SCI
        self.res_payment = round(self.first_payment * 0.87)

        for i in range(2, self.cupn_total + 1):
            self.res_payment += self.payment * 0.87

        return self.res_payment

    def cupnAndLots(self):
        self.payment = self.lots * (self.nominal * (self.percent / ((self.cupn_in_one_year * 100))))
        self.first_payment = (self.payment - self.lots * self.SCI) * 0.87

        return self.first_payment

        
        




