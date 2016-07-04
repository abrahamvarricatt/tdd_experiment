# When no sensors are installed what does hotel script return ?

from scripttest import TestFileEnvironment


def test_default_data():
    env = TestFileEnvironment('./test-output')
    result = env.run('../hotel_automation.py ../tests/functional_tests/no_sensor/input01.txt')
    assert 'Total floors = 2' in result.stdout
    assert 'Main corridors per floor = 1' in result.stdout
    assert 'Sub corridors per floor = 2' in result.stdout
    assert 'Sensors installed: = False' in result.stdout


def test_custom_floor_number():
    env = TestFileEnvironment('./test-output')
    result = env.run('../hotel_automation.py --floors=4 ../tests/functional_tests/no_sensor/input01.txt')
    assert 'Total floors = 4' in result.stdout

