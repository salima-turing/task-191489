import logging
import requests
import random
import time

# Dummy IoT device data
DEVICE_ID = "dummy_device_123"
SAAS_LOGGING_URL = "http://localhost:8000/log"


def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    return logger


def simulate_device_behaviour(logger):
    while True:
        # Simulate device events and failures
        event_type = random.choice(["temperature_update", "error", "status_change"])
        if event_type == "error":
            message = f"Device {DEVICE_ID} encountered an error! Sensor malfunction."
            logger.error(message)
            send_log_to_saas(message, logger, level="ERROR")
        else:
            value = random.randint(20, 30)
            message = f"{event_type}: Device {DEVICE_ID} reports temperature: {value}°C"
            logger.info(message)
            send_log_to_saas(message, logger)

        time.sleep(random.uniform(5, 10))


def send_log_to_saas(message, logger, level="INFO"):
    try:
        log_data = {
            "device_id": DEVICE_ID,
            "message": message,
            "level": level
        }
        response = requests.post(SAAS_LOGGING_URL, json=log_data)
        response.raise_for_status()
        logger.info(f"Log sent to SaaS: {message}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error sending log to SaaS: {e}")


if __name__ == "__main__":
    logger = setup_logging()
    simulate_device_behaviour(logger)
