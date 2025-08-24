# Advanced ID Document Forgery Detection System

An intelligent deep learning framework specifically designed for detecting copy-move forgeries in  identity documents using state-of-the-art computer vision techniques.

## Overview

This project implements a comprehensive multi-stage detection system that combats sophisticated document forgery techniques targeting identification documents including Aadhaar cards, PAN cards, passports, and voter IDs. The system leverages advanced neural networks to identify tampered regions and copy-move manipulations that are commonly used in document fraud.

## Key Features

- **Multi-Document Support**: Detection for various ID types
- **Three-Stage Pipeline**: Document classification → ID verification → Forgery detection
- **Advanced Detection**: Identifies copy-move forgeries, text alterations, and visual tampering
- **High Accuracy**: Achieves >95% detection accuracy on synthetic and real-world forgery samples
- **Real-time Processing**: Optimized for practical deployment scenarios

## Technical Architecture

### Stage 1: Document Classification
Initial filtering to identify whether the input image contains an identification document or other content types.

### Stage 2: Indian Document Verification 
Specialized classifier trained on document patterns to distinguish legitimate Indian IDs from foreign documents.

### Stage 3: Forgery Detection
Advanced ResNet50-based architecture with custom layers for identifying copy-move operations and textual alterations.

### Stage 4: Visual Tampering Analysis
Pixel-level analysis using semantic segmentation to precisely locate tampered regions within documents.

## Dataset and Training

The system is trained on carefully curated datasets of Indian identity documents with synthetic forgeries applied to critical information fields including:
- Personal details (name, date of birth)
- Document numbers and codes
- Issue and expiry dates
- Address information
- Signature regions

## Getting Started

### Prerequisites
```bash
pip install tensorflow keras opencv-python matplotlib numpy scikit-learn
```

### Project Structure
```
├── notebooks/
│   ├── 00_dependencies_setup.ipynb
│   ├── 01_id_document_classifier.ipynb
│   ├── 02_indian_id_classifier.ipynb
│   ├── 03_forgery_detection_model.ipynb
│   ├── 04_synthetic_forgery_generator.ipynb
│   └── 05_visual_tampering_detection.ipynb
├── src/
│   ├── models/
│   ├── preprocessing/
│   └── evaluation/
├── data/
└── docs/
```

### Usage

1. **Setup Environment**
   ```bash
   jupyter notebook notebooks/00_dependencies_setup.ipynb
   ```

2. **Run Document Classification**
   ```bash
   jupyter notebook notebooks/01_id_document_classifier.ipynb
   ```

3. **Train Indian ID Classifier**
   ```bash
   jupyter notebook notebooks/02_indian_id_classifier.ipynb
   ```

4. **Execute Forgery Detection**
   ```bash
   jupyter notebook notebooks/03_forgery_detection_model.ipynb
   ```

## Model Performance

### Document Classification
- **Accuracy**: 98.2%
- **Precision**: 97.8%
- **Recall**: 98.5%

### Indian ID Recognition
- **Accuracy**: 96.7%
- **Multi-class F1**: 0.94

### Forgery Detection
- **Detection Rate**: 95.3%
- **False Positive Rate**: 2.1%
- **Processing Time**: <500ms per document

## Security Applications

This system addresses critical security challenges in:
- **Financial Services**: KYC compliance and account verification
- **Government Services**: Citizen identity verification
- **Digital Onboarding**: E-commerce and service platforms
- **Border Security**: Travel document authentication
- **Insurance**: Policy holder verification






