# check our hello world output

from scripttest import TestFileEnvironment

def test_running_location():
    env= TestFileEnvironment('./test-output')
    result = env.run('../tempAA.py', expect_error=False)
    print "output = " + result.stdout
    assert result.stdout.startswith('Hello world')


