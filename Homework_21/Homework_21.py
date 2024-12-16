import logging
from datetime import datetime, timedelta

def setup_logger():
    log_formatter = logging.Formatter(
        '%(asctime)s - %(message)s - %(name)s - %(funcName)s - %(levelname)s')
    file_handler = logging.FileHandler('./hb_test.log')
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.DEBUG)

    logger = logging.getLogger("log_event")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.propagate = False
    return logger

logger = setup_logger()

def read_log(input_file = "hblog.txt", key = "Key TSTFEED0300|7E3E|0400"):
    filtered_log = []
    with open(input_file, "r") as log_file:
        for line in log_file:
            if key in line:
                filtered_log.append(line.strip())
    print(filtered_log)
    return filtered_log

def timestamp(line_with_key):
    try:
        timestamp_str = line_with_key[line_with_key.find("Timestamp ") + 10:line_with_key.find("Timestamp ") + 18]
        return datetime.strptime(timestamp_str, "%H:%M:%S")
    except (ValueError, AttributeError) as e:
        logger.error(f"Error with timestamp: {line_with_key}, {e}")
        return None

def heartbeat(filtered_log):
    for i in range(len(filtered_log) - 1):
        time_1 = timestamp(filtered_log[i])
        time_2 = timestamp(filtered_log[i + 1])

        if time_1 and time_2:
            time_difference = time_2 - time_1
            if timedelta(seconds=31) < time_difference < timedelta(seconds=33):
                logger.warning(
            f"WARNING! Time difference = {time_difference} seconds")
            elif time_difference >= timedelta(seconds=33):
                logger.error(f"ERROR! Time difference >= {time_difference} seconds ")
            else:
                logger.info(f"Don't worry! The heartbeat is not in the searching bad range")
        else:
            logger.error("ERROR! Failed to parse timestamps. Values: "
                     f"time_1={time_1}, time_2={time_2}")


def function_scope():
    input_file = "hblog.txt"
    key = "Key TSTFEED0300|7E3E|0400"
    filtered_log = read_log(input_file, key)

    heartbeat(filtered_log)

if __name__ == "__main__":
    function_scope()


