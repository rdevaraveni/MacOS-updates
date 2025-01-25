#!/usr/bin/python3
# This script will auto update packages

import subprocess
import logging
from datetime import datetime

# Configure logging
log_file = 'update_mac_apps.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s - %(levelname)s: %(message)s')

def update_brew_packages():
    try:
        # Log start time
        logging.info(f'Starting update at {datetime.now()}')

        # Update Homebrew itself
        logging.info('Updating Homebrew...')
        subprocess.run(['arch', '-arm64', 'brew', 'update'])

        # List outdated packages
        outdated_packages = subprocess.check_output(['arch', '-arm64', 'brew', 'outdated']).decode('utf-8').splitlines()

        if not outdated_packages:
            logging.info('No packages to update.')
        else:
            logging.info('Updating the following packages:')
            for package in outdated_packages:
                logging.info(f'Updating {package}')
                subprocess.run(['arch', '-arm64', 'brew', 'upgrade', package])

        # Clean up
        logging.info('Cleaning up...')
        subprocess.run(['arch', '-arm64', 'brew', 'cleanup'])

        # Log finish time
        logging.info(f'Update completed at {datetime.now()}')

    except Exception as e:
        logging.error(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    update_brew_packages()
