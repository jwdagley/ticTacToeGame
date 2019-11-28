# -*- coding: utf-8 -*-
import os
import kaggle as kg
import logging
from dotenv import load_dotenv, find_dotenv 

def get_logger():
    '''
    get the logger
    '''
    logger = logging.getLogger(__name__)
    logger.info('getting raw data')
    
    
def download_data_from_kaggle():
    '''
    use kaggle api to download files with username and key from .env file
    '''
    # find .env automatically by walking up directories until it's found
    dotenv_path = find_dotenv()
    # load up the entries as environmental variables
    load_dotenv(dotenv_path)

    # get kaggle username and password from .env file
    os.environ['KAGGLE_USERNAME']  = os.environ.get("KAGGLE_USERNAME")
    os.environ['KAGGLE_KEY'] = os.environ.get("KAGGLE_PASSWORD")
    
    # authenticate with kaggle api and download
    kg.api.authenticate()
    os.system('kaggle competitions download -c "titanic" -p ..\\data\\raw')



def main(project_dir):
    '''
    main method
    '''
    get_logger()
    download_data_from_kaggle()
    

if __name__ == '__main__':
    # getting the root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - $(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    
    main(project_dir)
