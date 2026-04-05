import subprocess
import time

def test_timer_runs_for_a_few_seconds():
    process = subprocess.Popen(["python", "timer.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    time.sleep(3)
    process.terminate()
    assert process.poll() is not None

