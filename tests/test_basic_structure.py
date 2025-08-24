"""
Basic tests for the Indian Document Forgery Detection System
"""

import unittest
import sys
import os

# Add src to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestProjectStructure(unittest.TestCase):
    """Test that the project structure is set up correctly."""
    
    def setUp(self):
        self.project_root = os.path.dirname(os.path.dirname(__file__))
    
    def test_required_directories_exist(self):
        """Test that all required directories are present."""
        required_dirs = ['src', 'notebooks', 'data', 'docs', 'tests']
        
        for directory in required_dirs:
            dir_path = os.path.join(self.project_root, directory)
            self.assertTrue(
                os.path.exists(dir_path),
                f"Required directory '{directory}' does not exist"
            )
    
    def test_required_files_exist(self):
        """Test that all required files are present."""
        required_files = [
            'README.md',
            'LICENSE',
            'requirements.txt',
            'setup.py',
            '.gitignore',
            'CONTRIBUTING.md'
        ]
        
        for filename in required_files:
            file_path = os.path.join(self.project_root, filename)
            self.assertTrue(
                os.path.exists(file_path),
                f"Required file '{filename}' does not exist"
            )
    
    def test_notebooks_exist(self):
        """Test that all expected notebooks are present."""
        expected_notebooks = [
            '00_dependencies_setup.ipynb',
            '01_id_document_classifier.ipynb',
            '02_indian_id_classifier.ipynb',
            '03_forgery_detection_model.ipynb',
            '04_synthetic_forgery_generator.ipynb',
            '05_visual_tampering_detection.ipynb'
        ]
        
        notebooks_dir = os.path.join(self.project_root, 'notebooks')
        
        for notebook in expected_notebooks:
            notebook_path = os.path.join(notebooks_dir, notebook)
            self.assertTrue(
                os.path.exists(notebook_path),
                f"Expected notebook '{notebook}' does not exist"
            )
    
    def test_src_modules_exist(self):
        """Test that source modules are properly structured."""
        src_modules = ['models', 'preprocessing', 'evaluation']
        src_dir = os.path.join(self.project_root, 'src')
        
        # Test main __init__.py
        self.assertTrue(
            os.path.exists(os.path.join(src_dir, '__init__.py')),
            "Main src/__init__.py does not exist"
        )
        
        # Test module directories
        for module in src_modules:
            module_dir = os.path.join(src_dir, module)
            self.assertTrue(
                os.path.exists(module_dir),
                f"Module directory '{module}' does not exist"
            )
            self.assertTrue(
                os.path.exists(os.path.join(module_dir, '__init__.py')),
                f"Module '{module}' __init__.py does not exist"
            )


class TestImports(unittest.TestCase):
    """Test that basic imports work."""
    
    def test_src_import(self):
        """Test that the src package can be imported."""
        try:
            import src
            self.assertIsNotNone(src.__version__)
        except ImportError as e:
            self.fail(f"Could not import src package: {e}")


if __name__ == '__main__':
    unittest.main()