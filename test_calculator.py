from calculator import calculate_performance, get_results
def test_calculator_score():
   scores = calculate_performance(10, 100, 100)
   assert scores == 334

def test_pass_get_results():
   results = get_results(51)
   assert results == "PASS"