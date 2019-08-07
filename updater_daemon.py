# updater_daemon.py
from importlib import util
import shutil
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filename='C:\\updater.log', filemode='a')
log = logging.getLogger(__name__)

if __name__ == '__main__':

    spec = util.spec_from_file_location('updater', 'Z:\\task.py')
    module = util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        shutil.copyfile("C:\\updater.log", "Z:\\updater.log")
    except FileNotFoundError:
        log.debug("Can't find file with tasks. Continuing to monitor...")
