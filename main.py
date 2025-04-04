from calendar import month

import datetime

import matplotlib.pyplot as pyplot

import pandas as pd
from pandas import DataFrame
from pandas.io.pytables import DataCol

from utils.normalize_dataset import normalize_dataset
from utils.date_hist_plot import date_hist_plot

# Загрузка и нормализация датасета
normalized_dataset: DataFrame = normalize_dataset(path="./data/raw.json", output_path="./data/raw-normalized.json")
print(normalized_dataset.count())
print(normalized_dataset.describe())

# Граффик первоначальный подач
submit_set = normalized_dataset["ApplicationSubmitted"].map(
    lambda date: datetime.datetime.fromtimestamp(date))

date_hist_plot(submit_set, chart_title="Количество первоначальных подач по месяцам", xlabel="Месяц",
               ylabel="Количество подач")
