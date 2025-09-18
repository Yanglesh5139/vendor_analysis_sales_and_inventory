import pandas as pd
import os
from sqlalchemy import create_engine
import time
import logging 
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from utils.log_utils import get_ingestion_logger

logger = get_ingestion_logger()



engine=create_engine('sqlite:///inventory.db', echo=False)


def ingest_db(df, table_name, engine):
    try:
        df.to_sql(table_name, con=engine, if_exists='replace', index=False)
        logger.info(f"Data ingested successfully into the {table_name} table.")
    except Exception as e:
        logger.error(f"Error ingesting data into the {table_name} table: {e}")

def process_files(engine):
    start=time.time()
    try:
        for file in os.listdir('data'):
            if file.endswith('.csv'):
                df=pd.read_csv(f'data/{file}')
                logger.info(f"Read file: {file}")
                ingest_db(df,file.split('.')[0],engine)
    except Exception as e:
        logger.error(f"Error processing files: {e}")   
    end=time.time()
    logger.info(f"Processing time: {end-start} seconds")
    logger.info("All files processed and ingested successfully.")








