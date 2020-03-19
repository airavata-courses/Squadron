import unittest 

from post_processing import total_cost
from post_processing import compute 

class Test(unittest.TestCase):

	def test_cost(self):
		print("Testing cost total")
		res = total_cost(1)
		self.assertEqual(res,35)


	def test_compute(self):
		print("Testing compute ")
		t = b'{"house_area": 2, "PinCode": 47408, "Months": [1, 3], "RequestId": "1221", "Data": [{"MonthName": "January", "HighTemp": 36.5, "AvgTemp": 27.9, "LowTemp": 19.3, "Cdd": 0, "Hdd": 1151, "Rain": 2.66, "Zip": "47408", "MonthNumber": 1}, {"MonthName": "March", "HighTemp": 52.4, "AvgTemp": 42, "LowTemp": 31.6, "Cdd": 0, "Hdd": 713, "Rain": 3.66, "Zip": "47408", "MonthNumber": 3}], "Status": "ok", "model_result": 7.078400000000001, "post_processed_result": 247.74400000000003, "status": "COMPLETED"}'
		k = {"house_area": 2, "PinCode": 47408, "Months": [1, 3], "RequestId": "1221", "Data": [{"MonthName": "January", "HighTemp": 36.5, "AvgTemp": 27.9, "LowTemp": 19.3, "Cdd": 0, "Hdd": 1151, "Rain": 2.66, "Zip": "47408", "MonthNumber": 1}, {"MonthName": "March", "HighTemp": 52.4, "AvgTemp": 42, "LowTemp": 31.6, "Cdd": 0, "Hdd": 713, "Rain": 3.66, "Zip": "47408", "MonthNumber": 3}], "Status": "ok", "model_result": 7.078400000000001}
		res=compute(k)
		self.assertEqual(res,t)



if __name__ == '__main__':
	print("Testing started")
	unittest.main()
