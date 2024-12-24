from dataclasses import dataclass


@dataclass
class ColBERTConfig:
    experiment_path: str = "/app/index/experiments/msmarco"
    index_name: str = "ir"
    index_url: str = "https://drive.google.com/uc?&id=1Y1Eee4mHQ-jDvBUNehFfEmMj-r9iNDcf"
    folder_name: str = "experiments"

@dataclass
class BM25Config:
    experiment_path: str = "/app/index/experiments/bm25"
    arxiv_collections_url: str = "https://drive.google.com/uc?&id=18o8MduiMdkBOpa--6Nere7uGQNxJohaT"
    arxiv_collections_folder: str = "arxiv_collections"
    index_url: str = "https://drive.google.com/uc?&id=1WHVMtvlLvPL9bGMCq6l-XxGjFA6Zzzyp"
    index_folder: str = "index"
    embed_url: str = "https://drive.google.com/uc?&id=1Dbrbs1bHfbcVh9PRtxmJPQDDg9ypZTQw"
    embed_filename: str = "document_embedded.json"
    embed_folder: str = "experiment/data"