#!/usr/bin/env python3
"""
app.py

eBook Library Parser
"""
from .log_init import setup_logging

logger = setup_logging()


def main():
    logger.debug("Entering main.")
    logger.info("Printing default message")
    print(f"Successfully installed your project file: pybrary")


if __name__ == "__main__":
    logger.debug("Running as a module.")
    main()