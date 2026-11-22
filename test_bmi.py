import subprocess
from BMI import calculate_bmi, get_bmi_category, ideal_weight_range, calculate_bmi_prime

def test_bmi_calculation():
    result = subprocess.run(["python", "BMI.py"], input="1\n70\n1.75\n", capture_output=True, text=True)
    assert "22.86" in result.stdout

def test_ideal_weight():
    result = subprocess.run(["python", "BMI.py"], input="2\n1.75\n", capture_output=True, text=True)
    assert "56.66" in result.stdout

def test_bmi_category():
    assert get_bmi_category(17.0) == "Underweight"
    assert get_bmi_category(22.5) == "Normal weight"
    assert get_bmi_category(28.0) == "Overweight"
    assert get_bmi_category(31.0) == "Obese"

def test_ideal_weight_tuple():
    assert ideal_weight_range(1.75) == (56.66, 76.26)

def test_bmi_prime():
    assert calculate_bmi_prime(22.5) == 0.9

def test_bmi_direct():
    assert calculate_bmi(70, 1.75) == 22.86