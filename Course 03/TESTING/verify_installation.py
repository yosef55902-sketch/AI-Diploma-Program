#!/usr/bin/env python3
"""
Verify Installation Script
Tests that all required libraries are installed and working.
"""

import sys

def test_imports():
    """Test that all required libraries can be imported."""
    print("Testing library imports...")
    
    libraries = {
        'numpy': 'NumPy',
        'scipy': 'SciPy',
        'sklearn': 'scikit-learn',
        'matplotlib': 'Matplotlib',
        'seaborn': 'Seaborn',
    }
    
    failed = []
    
    for module, name in libraries.items():
        try:
            __import__(module)
            print(f"✅ {name} imported successfully")
        except ImportError as e:
            print(f"❌ {name} import failed: {e}")
            failed.append(name)
    
    if failed:
        print(f"\n❌ Installation incomplete. Failed libraries: {', '.join(failed)}")
        print("Run: pip install -r ../../requirements.txt")
        return False
    else:
        print("\n✅ All libraries installed and working!")
        return True

def test_jupyter():
    """Test that Jupyter is available."""
    try:
        import jupyter
        print("✅ Jupyter is installed")
        return True
    except ImportError:
        print("❌ Jupyter is not installed")
        print("Run: pip install jupyter")
        return False

if __name__ == '__main__':
    print("=" * 60)
    print("Installation Verification")
    print("=" * 60)
    print()
    
    imports_ok = test_imports()
    jupyter_ok = test_jupyter()
    
    print()
    print("=" * 60)
    if imports_ok and jupyter_ok:
        print("✅ All checks passed! You're ready to start.")
        sys.exit(0)
    else:
        print("❌ Some checks failed. Please fix the issues above.")
        sys.exit(1)

