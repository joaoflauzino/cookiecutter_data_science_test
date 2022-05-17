import logging
import pandas as pd
from pathlib import Path
from dotenv import find_dotenv, load_dotenv


class BuildFeatures(object):

    def __init__(self, path: str, destino: str) -> None:
        self.path = path
        self.destino = destino

    def leitura_arquivo(self) -> None:
        self.dataframe = pd.read_csv(self.path, sep=",")

    def _root(self, variaveis: list) -> None:
        variaveis_ = [i + '_root' for i in variaveis]
        self.dataframe[variaveis_] = self.dataframe[variaveis]**2

    def _division(self, variaveis: list) -> None:
        variaveis_ = [i + '_division' for i in variaveis]
        self.dataframe[variaveis_] = self.dataframe[variaveis]/2

    def main(self, variaveis_root, variaveis_division):
        """ Runs data processing scripts to turn raw data from (../raw) into
            cleaned data ready to be analyzed (saved in ../processed).
        """
        logger = logging.getLogger(__name__)
        logger.info('Construindo variáveis')
        self.leitura_arquivo()
        self._root(variaveis_root)
        self._division(variaveis_division)
        logger.info('Variáveis criadas!')
        return self.dataframe.to_csv(self.destino, sep=",")


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())
    origem = 'data/raw/IRIS.csv'
    destino = 'data/processed/processed_features.csv'
    variaveis_root = ['sepal_length', 'sepal_width']
    variaveis_division = ['sepal_width']
    features = BuildFeatures(origem, destino)
    features.main(variaveis_root, variaveis_division)
