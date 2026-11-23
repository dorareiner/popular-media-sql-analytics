import kagglehub

# Download the latest version of the dataset from Kaggle
path = kagglehub.dataset_download("mariaaqdas/popular-movies-and-tv-shows-dataset-2026")
print("Dataset downloaded to:", path)
