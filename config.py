# Project Configuration for Indian Document Forgery Detection System

# Model Parameters
MODEL_CONFIG = {
    "input_shape": (224, 224, 3),
    "batch_size": 32,
    "epochs": 20,
    "learning_rate": 0.001,
    "dropout_rate": 0.5
}

# Indian Document Classes
INDIAN_DOCUMENT_CLASSES = [
    "ind_id",           # General Indian ID
    "ind_passport",     # Indian Passport  
    "ind_aadhaar",     # Aadhaar Card
    "ind_pan",         # PAN Card
    "ind_voter",       # Voter ID
    "other_passport",   # Non-Indian Passport
    "other_id",        # Other Foreign ID
    "foreign_id",      # Foreign Document
    "corporate_id",    # Corporate ID
    "temp_id"          # Temporary Document
]

# Data Paths (adjust for your environment)
DATA_PATHS = {
    "dataset_root": "/content/indian-document-forgery-detection/dataset",
    "images": "/content/indian-document-forgery-detection/dataset/images",
    "annotations": "/content/indian-document-forgery-detection/dataset/annotations",
    "train": "/content/indian-document-forgery-detection/dataset/train",
    "validation": "/content/indian-document-forgery-detection/dataset/val", 
    "test": "/content/indian-document-forgery-detection/dataset/test"
}

# Training Configuration
TRAINING_CONFIG = {
    "train_split": 0.7,
    "validation_split": 0.2,
    "test_split": 0.1,
    "augmentation": True,
    "early_stopping": True,
    "patience": 5
}

# Detection Thresholds
DETECTION_THRESHOLDS = {
    "document_classification": 0.8,
    "indian_id_verification": 0.85,
    "forgery_detection": 0.75,
    "tampering_detection": 0.7
}