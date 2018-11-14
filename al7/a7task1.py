# -*- coding: utf-8 -*-


class Bond:
    """ Creating a class definition for class Bond """
    def __init__(self, maturity_value, maturity_time, coupon_rate=0, coupon_frequency=2):
        self.__maturity_value = maturity_value
        self.__maturity_time = maturity_time
        self.__coupon_rate = coupon_rate
        self.__coupon_frequency = coupon_frequency
        self.__yield_to_maturity = coupon_rate
        self.__price = maturity_value
    
    def __repr__(self):
        return '$%.2f-maturity %d-year %.4f%% bond, ytm= %.4f%%, price=$%.2f,duration=%.4f, convexity=%.4f' %(self.__maturity_value,
                                                                                self.__maturity_time,
                                                                                self.__coupon_rate*100,
                                                                                self.__yield_to_maturity*100,
                                                                                self.__price,
                                                                                self.get_duration(),
                                                                                self.get_convexity())
        
    
    def get_maturity_value(self):
        return self.__maturity_value

    def get_maturity_time(self):
        return self.__maturity_time
    
    def get_coupon_frequency(self):
        return self.__coupon_frequency
    
    def get_coupon_rate(self):
        return self.__coupon_rate
    
    def get_pmt_times(self):
         return [ i for i in range(1,self.__maturity_time*self.__coupon_frequency+1)]
        
    def get_coupon_amount(self):
        return self.__coupon_rate/self.__coupon_frequency*self.__maturity_value
    
    def get_price(self):
        return self.__price
        
    def get_yield_to_maturity(self):
        return self.__yield_to_maturity

    def get_cashflows(self):
        time_list = self.get_pmt_times()
        return [(int(t/(self.__coupon_frequency*self.__maturity_time))+self.__coupon_rate/self.__coupon_frequency)*self.__maturity_value for t in time_list]
    
    def get_discount_factors(self):
        time_list = self.get_pmt_times()
        return [1/(1+self.__yield_to_maturity/self.__coupon_frequency)**t for t in time_list]
        
    def calculate_price(self):
        time_list = self.get_pmt_times()
        cashflows = self.get_cashflows()
        df = self.get_discount_factors()
        pv_list = [cashflows[t-1]*df[t-1] for t in time_list ]
        return sum(pv_list)
    
    def set_yield_to_maturity(self, new_ytm):
        self.__yield_to_maturity = new_ytm
        self.__price = self.calculate_price()
        
    def calculate_yield_to_maturity(self, accuracy=0.0001):
        r0 = 0
        r1 = 0.5
        self.__yield_to_maturity = r1
        price_after = self.calculate_price()
        error_0 =  price_after-self.__price
        r2 = (r1+r0)/2
        while True:
            self.__yield_to_maturity = r2
            if abs(error_0)<=0.000001:
                break
            price_after = self.calculate_price()
            error_1 =  price_after-self.__price
            if error_0*error_1 <0:
                r0 = r1  
            r1 = r2
            error_0 = error_1
            r2 = (r0+r1)/2
    def set_price(self, price):
        self.__price = price
        self.calculate_yield_to_maturity()
        
    def get_duration(self):
        time_list = self.get_pmt_times()
        cashflows = self.get_cashflows()
        df = self.get_discount_factors()
        pv_list = [t*cashflows[t-1]*df[t-1] for t in time_list ]
        price_bound = self.calculate_price()
        return sum(pv_list)/price_bound/self.__coupon_frequency
    
    def get_convexity(self):
        time_list = self.get_pmt_times()
        cashflows = self.get_cashflows()
        df = self.get_discount_factors()
        pv_list = [(t+1)*t*cashflows[t-1]*df[t-1] for t in time_list ]
        price_bound = self.calculate_price()
        return sum(pv_list)/(1+self.__yield_to_maturity/self.__coupon_frequency)**2/(price_bound*self.__coupon_frequency)/self.__coupon_frequency
    
















    