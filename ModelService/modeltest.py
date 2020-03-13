#!/usr/bin/python
import unittest


from model import sum_rain
from model import compute
from model import water




class Test(unittest.TestCase):

	def test_rain_sum(self):
		print("Testing Rain Sum")
		k = {"house_area":2,"PinCode":47408,"Months":[1,3],"RequestId":"1221","Data":[{"MonthName":"January","HighTemp":36.5,"AvgTemp":27.9,"LowTemp":19.3,"Cdd":0,"Hdd":1151,"Rain":2.66,"Zip":"47408","MonthNumber":1},{"MonthName":"March","HighTemp":52.4,"AvgTemp":42,"LowTemp":31.6,"Cdd":0,"Hdd":713,"Rain":3.66,"Zip":"47408","MonthNumber":3}],"Status":"ok"}
		res = sum_rain(k)
		self.assertEqual(res,6.32)

	def test_water(self):
		print("Testing ")
		res =water(1,1)
		self.assertEqual(res,0.56)


	def test_compute(self):
		print("testing compute")
		k = {"house_area":2,"PinCode":47408,"Months":[1,3],"RequestId":"1221","Data":[{"MonthName":"January","HighTemp":36.5,"AvgTemp":27.9,"LowTemp":19.3,"Cdd":0,"Hdd":1151,"Rain":2.66,"Zip":"47408","MonthNumber":1},{"MonthName":"March","HighTemp":52.4,"AvgTemp":42,"LowTemp":31.6,"Cdd":0,"Hdd":713,"Rain":3.66,"Zip":"47408","MonthNumber":3}],"Status":"ok"}
		res = compute(k)
		p = {"house_area": 2, "PinCode": 47408, "Months": [1, 3], "RequestId": "1221", "Data": [{"MonthName": "January", "HighTemp": 36.5, "AvgTemp": 27.9, "LowTemp": 19.3, "Cdd": 0, "Hdd": 1151, "Rain": 2.66, "Zip": "47408", "MonthNumber": 1}, {"MonthName": "March", "HighTemp": 52.4, "AvgTemp": 42, "LowTemp": 31.6, "Cdd": 0, "Hdd": 713, "Rain": 3.66, "Zip": "47408", "MonthNumber": 3}], "Status": "ok", "model_result": 7.078400000000001}
		self.assertEqual(k,p)
		print("Testing compute Finished")


if __name__ == '__main__':
	print("Testing Model started ")
	unittest.main()
