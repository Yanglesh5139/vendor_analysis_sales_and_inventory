import pandas as pd
import sqlite3
import logging
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from get_vendor_summary import create_vendor_summary_table,clean_data,add_columns_from_json
from ingestion_script import process_files, ingest_db, engine
from utils.log_utils import get_main_logger
from utils.utils import QueryManager
logger=get_main_logger()

if __name__ == '__main__':
    conn=sqlite3.connect('inventory.db')
    config_file_path = 'utils/json_files/calculations.json'  # Path to your JSON configuration file
    manager=QueryManager()
    try:
        process_files(engine)
        summary_df=create_vendor_summary_table(conn,manager.get_query("create_vendor_summary_table"))
        logger.info(f"Summary DataFrame created with {len(summary_df)} records.")
        # logger.info(summary_df.head())
        if not summary_df.empty:
            
            cleaned_df=clean_data(summary_df)
            # logger.info(cleaned_df.head())
            final_df=add_columns_from_json(cleaned_df, config_file_path)
            ingest_db(final_df, 'vendor_summary', conn)
            logger.info("Vendor summary data cleaned and ingested successfully.")
            logger.info(f"Final DataFrame has {len(final_df)} records and columns: {final_df.columns.tolist()} ")
        else:
            logger.error("Summary DataFrame is empty. Skipping cleaning and ingestion.")
    except Exception as e:
        logger.error(f"Error in main execution: {e}")