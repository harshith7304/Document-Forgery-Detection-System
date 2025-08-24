# Quick Start Guide

## Installation

```bash
git clone https://github.com/harshith7304/proj.git
cd proj
pip install -r requirements.txt
```

## Running the Notebooks

Execute the notebooks in order:

1. **Dependencies Setup**: `notebooks/00_dependencies_setup.ipynb`
2. **Document Classification**: `notebooks/01_id_document_classifier.ipynb`  
3. **Indian ID Verification**: `notebooks/02_indian_id_classifier.ipynb`
4. **Forgery Detection**: `notebooks/03_forgery_detection_model.ipynb`
5. **Synthetic Data Generation**: `notebooks/04_synthetic_forgery_generator.ipynb`
6. **Visual Tampering Detection**: `notebooks/05_visual_tampering_detection.ipynb`

## Testing

Run tests to verify installation:

```bash
python -m unittest tests.test_basic_structure -v
```

## Configuration

Modify `config.py` to adjust:
- Model parameters
- Data paths  
- Detection thresholds
- Training configuration

## Supported Indian Document Types

- Aadhaar Card
- PAN Card
- Indian Passport
- Voter ID Card
- General Indian ID Documents

## Key Features

✅ Multi-stage detection pipeline  
✅ Indian document specialization  
✅ Copy-move forgery detection  
✅ Visual tampering analysis  
✅ Real-time processing capability  
✅ High accuracy (>95%)  

## Need Help?

- Check `CONTRIBUTING.md` for development guidelines
- Open an issue for bug reports or feature requests
- Refer to the detailed README.md for comprehensive information