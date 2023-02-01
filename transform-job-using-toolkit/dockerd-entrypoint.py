import sys
import subprocess
from subprocess import CalledProcessError
from retrying import retry
from sagemaker_inference import model_server


def _retry_if_error(exception):
    return isinstance(exception, CalledProcessError or OSError)

@retry(stop_max_delay=1000 * 50, retry_on_exception=_retry_if_error)
def _start_model_server():
    model_server.start_model_server()

def main():
    if sys.argv[1] == "serve":
        _start_model_server()

    # prevent docker exit
    subprocess.call(["tail", "-f", "/dev/null"])

main()
