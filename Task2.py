import self as self
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
            forecasts_text=forecasts['text']
            if forecasts_text.find('Rain') != -1:
                self.rainy_days.append(day_count)
            day_count +=1
		#	print (forecasts['date'])
    	#	print (forecasts['high'])
    	#	print (forecasts['low'])

def main():
	city=input("Enter the city:")
	weatherobj=WeatherForecast(city)
	weatherobj.lookup_name()

if __name__ == "__main__":
	main()