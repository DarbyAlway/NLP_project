import mlflow
from mlflow.models import infer_signature
from mlflow.data.huggingface_dataset import HuggingFaceDataset
from time import time
import pandas as pd
from datasets import load_dataset

# Use Flair Benchmark Model
from flair.data import Sentence
from flair.models import SequenceTagger

# Tracking Server Config
mlflow.set_experiment('NER on CoNLL 2003')
mlflow.set_tracking_uri(uri="http://127.0.0.1:5678")

# Load Conll2003 using datasets library
conll_train_ds = mlflow.HuggingFaceDataset("Rosenberg/conll2003", split="train")
conll_test_ds = mlflow.HuggingFaceDataset("Rosenberg/conll2003", split="test")
conll_valid_ds = mlflow.HuggingFaceDataset("Rosenberg/conll2003", split="validation")

