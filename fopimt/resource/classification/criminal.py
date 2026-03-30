from sklearn.model_selection import train_test_split
from ...modul import Modul
import pandas as pd

class Criminal(Modul):

    @classmethod
    def get_short_name(cls) -> str:
        return "resource.criminal"

    @classmethod
    def get_long_name(cls) -> str:
        return "Criminal dataset"

    @classmethod
    def get_description(cls) -> str:
        return "Custom Criminal dataset"

    def __load_dataset(self) -> pd.DataFrame:
        try:
            majetkove_dict = pd.read_excel("./files/Majetkové přestupky.xlsx", sheet_name=None)
            poradek_dict = pd.read_excel("./files/Veřejný pořádek.xlsx", sheet_name=None)

            majetkove = pd.concat(majetkove_dict.values(), ignore_index=True)
            poradek = pd.concat(poradek_dict.values(), ignore_index=True)
        except FileNotFoundError:
            raise FileNotFoundError("Dataset files not found. Please ensure the files are in the correct path.")

        df = pd.concat([majetkove, poradek], ignore_index=True)
        return df

    def __preprocess_data(self, df: pd.DataFrame) -> dict:
        copy = df.copy()
        copy = copy.drop(columns=["Číslo jednací ", "Typ podrobně ", "Způsob řešení "])
        datetime_col = pd.to_datetime(copy['Datum a čas '])
        copy['Datum'] = datetime_col.dt.date
        copy['Čas'] = datetime_col.dt.time
        copy = copy.drop(columns=["Datum a čas "])
        return copy


    @staticmethod
    def full() -> dict:
        """
        Returns full Criminal dataset.
        """
        raw = self.__load_dataset()
        preprocessed = self.__preprocess_data(raw)

        raise NotImplementedError("The full dataset is not implemented yet. This is a placeholder for future implementation.")

        # x_train, x_test, y_train, y_test = train_test_split(
        #     breast_cancer.data, breast_cancer.target, test_size=0.2, random_state=42
        # )

        # train = {"data": x_train, "target": y_train}
        # test = {"data": x_test, "target": y_test}

        # return {
        #     "train_data": {"X": train["data"], "y": train["target"]},
        #     "test_data": {"X": test["data"], "y": test["target"]},
        # }
