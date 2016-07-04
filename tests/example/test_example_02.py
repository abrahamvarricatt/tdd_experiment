# check our hello world output

from scripttest import TestFileEnvironment

def test_running_location():
    env= TestFileEnvironment('./test-output')
    result = env.run('py.test --version', expect_error=True)
    print "output = " + result.stderr
    assert result.stderr.startswith('This is pytest version')


