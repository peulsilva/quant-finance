import pandas as pd

class Splitter():
    """Class splits data into validation and test. 
    train_size + test_size may be different than 1 
    to avoid lookahead bias
    """    

    def __init__(
        self,
        train_size : float = 0.6,
        test_size : float = 0.3
    ) -> None:

        self.train_size = train_size,
        self.test_size = test_size

    def split(self, df : pd.DataFrame):
        end_validation_date = df['date']\
            .quantile(self.train_size)

        start_test_date = df['date']\
            .quantile(1-self.test_size)

        validation_df = df[df['date'] <= end_validation_date]
        test_df = df[df['date'] >= start_test_date]

        return validation_df, test_df