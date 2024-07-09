from tqdm import tqdm
from pathlib import Path
from cnnClassifier.entity import DataIngestionConfig
from cnnClassifier import logger
from zipfile import ZipFile

import os
import urllib.request as request



class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        if not Path(self.config.local_data_file).exists():
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )

    
    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
    
    
    def _preprocess(self, zf: ZipFile, f: str, working_dir: Path):
        target_filepath = Path(working_dir) /  f
        if not Path(target_filepath).exists():
            zf.extract(f, working_dir)
        
        if Path(target_filepath).stat().st_size == 0:
            Path(target_filepath).unlink()

    

    
    def unzip_and_clean(self):
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in updated_list_of_files:
                self._preprocess(zf, f, self.config.unzip_dir)