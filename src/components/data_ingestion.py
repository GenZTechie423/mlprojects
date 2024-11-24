import os
import sys
import pandas as pd

# Add the project root to sys.path
project_root = os.path.abspath("C:/Users/sudhr/Downloads/mlprojects")
if project_root not in sys.path:
    sys.path.insert(0, project_root)

print(sys.path)
from src.exceptions import CustomException
from src.logger import logging

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")
