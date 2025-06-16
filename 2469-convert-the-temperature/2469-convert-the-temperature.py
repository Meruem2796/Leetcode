class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        Kelvin = round(celsius + 273.15, 5)
        Fahrenheit = round(celsius * 1.8 + 32.00, 5)
        ans = [Kelvin, Fahrenheit]
        return ans
