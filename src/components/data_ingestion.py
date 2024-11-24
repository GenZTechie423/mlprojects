import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Add the project root to sys.path
project_root = os.path.abspath("C:/Users/sudhr/Downloads/mlprojects")
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.exceptions import CustomException
from src.logger import logging
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

print(sys.path)


@dataclass
class DataIngestionConfig:
    # Define paths for saving train, test, and raw data
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        # Initialize the ingestion config
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        # Start logging for the data ingestion process
        logging.info("Entered the data ingestion method or component")
        try:
            # Absolute path for the dataset (change as per your dataset location)
            absolute_data_path = (
                r"C:\Users\sudhr\Downloads\mlprojects\Notebooks\Data\stud.csv"
            )
            print(f"Attempting to read data from: {absolute_data_path}")

            # Reading the dataset
            df = pd.read_csv(absolute_data_path)
            logging.info("Read the dataset into the dataframe")

            # Create the artifacts directory (train/test/raw data will be saved here)
            artifacts_dir = os.path.dirname(self.ingestion_config.train_data_path)
            print(f"Attempting to create directory: {artifacts_dir}")
            os.makedirs(
                artifacts_dir, exist_ok=True
            )  # Create directory if it doesn't exist
            print(f"Directory created successfully: {artifacts_dir}")

            # Save the raw data (df) to the artifacts folder
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            print(f"Raw data saved to: {self.ingestion_config.raw_data_path}")
            logging.info(f"Raw data saved to: {self.ingestion_config.raw_data_path}")

            # Train test split
            print("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Save train and test datasets
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )
            logging.info("Ingestion of data is complete")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )

        except Exception as e:
            print(f"Error: {str(e)}")
            logging.error(f"Error: {str(e)}")
            raise CustomException(e, sys)


if __name__ == "__main__":
    # Create an instance of DataIngestion and initiate the data ingestion process
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(
        train_data, test_data
    )

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))
