# check our hello world output

from scripttest import TestFileEnvironment

def test_hello_world():
    env= TestFileEnvironment('./test-output')
    result = env.run('../tempAA.py', expect_error=False)
    print "output = " + result.stdout
    assert result.stdout.startswith('Hello world')

def test_helloworld_dup():
    env= TestFileEnvironment('./test-output')
    result = env.run('../tempAA.py', expect_error=False)
    print "output = " + result.stdout
    assert result.stdout.startswith('Hello world')


