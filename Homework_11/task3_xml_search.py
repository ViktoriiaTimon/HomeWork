import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("log_output.log"),
                    ])
logger = logging.getLogger(__name__)

tree = ET.parse('groups.xml')
root_el = tree.getroot()

for sub_el in root_el.findall('group'):
    timing_exbytes = sub_el.find('timingExbytes')
    if timing_exbytes is not None:
        incoming = timing_exbytes.find('incoming')
        if incoming is not None:
            print(f"Incoming value for group {sub_el.find('number').text}: {incoming.text}")
    else:
        print(f"Incoming value for group {sub_el.find('number').text}: Not found")

        logger.info(f"Incoming value for group {sub_el.find('number').text}: {incoming.text}")