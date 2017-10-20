import weather


class WeatherForecast():
	def __init__(self,city):
		self.city=city
		self.weather_handle=weather.Weather()

	def lookup_name(self):
		# Lookup via location name.
		weather_handle=weather.Weather()
		location = 	self.weather_handle.lookup_by_location(self.city)
		condition = location.condition()
		print(condition['text'])
    def max_fn(li):
        r=0
        max = 0
        for i in range(len(li)):
            if int(li[i])>max:
                max=int(li[i])
                r = i
            i+=1
        return r

    def min_fn(li):
        r = 0
        min = 1000
        for i in range(len(li)):
            if int(li[i]) > min:
                min = int(li[i])
                r = i
            i += 1
        return r

	def get_forecast(self):
        # Get weather forecasts for the upcoming days.
		self.dates=[]
		self.high_temp=[]
		self.low_temp=[]
        self.rainy_days=[]
        self.current_cond=""
        location = 	self.weather_handle.lookup_by_location(self.city)
		condition = location.condition()
        day_count=0
		forecastlist= location.forecast()[:5]
		for forecasts in location.forecast():
			self.dates.append(forecasts['date']
			self.high_temp.append(forecasts['high']
			self.low_temp.append(forecasts['low']
            forecast_text=str(forecasts['text'])
            if forecasts_text.find('Rain') != -1:
                self.rainy_days.append(day_count)
            day_count +=1

    def print_forecast(self):
        print("Highest temp on:",self.dates[self.find_max(self.high_temp)])
        print("Lowest temp on:",self.dates[self.find_min(self.low_temp)])
        if (len(self.rainy_days)) > 0:
            print("Rain will be in the follwoign days")
            for i in self.rainy_days:
                print(self.dates[i]))

def main():
	city=input("Enter the city:")
	weatherobj=WeatherForecast(city)
	weatherobj.lookup_name()
    weatherobj.get_forecast()
    weatherobj.print_forcast()


if __name__ == "__main__":
	main()