from cnnClassifier import logger
from cnnClassifier.pipeline.Stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.Stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.Stage_03_model_training import ModelTrainingPipeine


STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n==========')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Prepare Base Model'

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n==========')
except Exception as e:
    logger.exception(e)
    raise e

try:
    logger.info(f'>>>>>> stage {STAGE_NAME} started <<<<<<')
    obj = ModelTrainingPipeine()
    obj.main()
    logger.info(f'>>>>>> stage {STAGE_NAME} completed <<<<<< \n\n==========')

except Exception as e:
    logger.exception(e)
    raise e