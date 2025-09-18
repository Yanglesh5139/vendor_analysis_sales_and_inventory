import json
import os
from typing import Optional

class QueryManager:
    def __init__(self, json_file: str = "utils/json_files/queries.json"):
        self.json_file = json_file
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"Query file '{json_file}' not found")
        
        with open(json_file, 'r', encoding='utf-8') as file:
            self.queries = json.load(file)
    
    def get_query(self, query_name: str) -> str:
        """Get a specific query in triple-quoted format"""
        if query_name not in self.queries:
            available = list(self.queries.keys())
            raise KeyError(f"Query '{query_name}' not found. Available: {available}")
        
        return f'{self.queries[query_name]}'
    
    def get_all_queries(self) -> dict:
        """Get all queries in triple-quoted format"""
        return {key: f'{value}' for key, value in self.queries.items()}

    def list_queries(self) -> list:
        """List all available query names"""
        return list(self.queries.keys())

def load_json(json_file_path,required_key):
    """Load column definitions from JSON file"""
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data[required_key]
