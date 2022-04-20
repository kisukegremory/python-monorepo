from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd


class YesAndNoToBinaryTransformer(BaseEstimator, TransformerMixin):
    def fit(self, x, y = None):
        self.binary_cols = x.columns[x.nunique() == 2]
        return self
    def transform(self, x, y = None):
        x_ = x.copy()
        for col in self.binary_cols:
            x_[col] = x_[col].replace({'No':0,'Yes':1})
        return x_
class ReplaceTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, col: str, to_replace: list, values: list):
        self.col = col
        self.to_replace = to_replace
        self.values = values
    def fit(self, x: pd.DataFrame, y = None):
        return self
    def transform(self, x: pd.DataFrame, y = None):
        x_ = x.copy()
        x_[self.col].replace(self.to_replace, self.values, inplace=True)
        return x_
class GetDummiesTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, dummies_kwargs:dict):
        self.dummies_kwargs = dummies_kwargs
    def fit(self, x: pd.DataFrame, y = None):
        return self
    def transform(self, x: pd.DataFrame, y = None):
        x_ = x.copy()
        x_ = pd.get_dummies(x_, **self.dummies_kwargs)
        return x_