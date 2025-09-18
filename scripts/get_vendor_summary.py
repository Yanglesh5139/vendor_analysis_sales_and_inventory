import sqlite3
import pandas as pd
import logging
import json
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from ingestion_script import ingest_db
from utils.utils import load_json
from utils.log_utils import get_vendor_summary_logger

logger = get_vendor_summary_logger()

def create_vendor_summary_table(conn,query_name):
    try:
        vendor_sales_summary=pd.read_sql(query_name,conn)
        logger.info("Vendor summary table created successfully")
        return vendor_sales_summary
    except Exception as e:
        logger.error(f"Error creating vendor summary table: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error


def clean_data(df):
    try:
        #change the ActualVolume column data type to float64
        df['Volume'] = df['Volume'].astype('float64')
        logger.info("Changed ActualVolume column to float64")
        #change the null values to 0
        df.fillna(0, inplace=True)
        logger.info("Null values handled successfully")
        #remove the whitespaces from VendorName
        df['VendorName'] = df['VendorName'].str.strip()
        df['Description'] = df['Description'].str.strip()
        logger.info("Whitespaces removed from VendorName and Description")
        logger.info("Data cleaned successfully")
        logger.info(f"size of dataframe after cleaning: {df.shape}")
        
    except Exception as e:
        logger.error(f"Error cleaning data: {e}")
    return df  # Return the original DataFrame in case of error




def add_columns_from_json(df, json_file_path):
    """Add calculated columns based on JSON definitions"""
    column_defs = load_json(json_file_path,'column_definitions')
    result_df = df.copy()
    
    for column_name, config in column_defs.items():
        try:
            # Use pandas eval to calculate the formula
            result_df[column_name] = result_df.eval(config['formula'])
            logger.info(f"Calculated column '{column_name}' added successfully with formula: {config['formula']}")
                
        except Exception as e:
            logger.error(f"Error calculating column '{column_name}': {e}")

    return result_df

