# APKGuard - Androguard based APK analysis and classification project

## Overview

This project demonstrates an end-to-end pipeline for extracting permissions from Android APKs using Androguard, constructing a binary permission matrix, training a Random Forest classifier to distinguish between malicious and benign apps, and evaluating the model on new APK samples.

## Prerequisites

* Python 3.6 or higher
* [Androguard](https://github.com/androguard/androguard) (`pip install androguard`)
* NumPy (`pip install numpy`)
* scikit-learn (`pip install scikit-learn`)
* Joblib (`pip install joblib`)

## Repository Structure

```
├── extract_permissions_log.py      # Extracts permissions from APKs and saves to text files
├── permission_matrix.py           # Builds a NumPy matrix from permission logs
├── train_ml_model.py              # Trains Random Forest model on the permission matrix
├── test_ml_model.py               # Predicts labels on new APKs using the trained model
├── permission_matrix.npy          # Saved binary matrix (auto-generated)
├── trained_model.pkl              # Saved Random Forest model (auto-generated)
└── README.md                      # Project documentation
```

## Usage Guide

1. **Extract Permissions**

   ```bash
   python extract_permissions_log.py
   ```

   * Scans up to 10 APKs in `~/Downloads/APKs`
   * Saves permission logs under `~/Downloads/Permissions`

2. **Generate Permission Matrix**

   ```bash
   python permission_matrix.py
   ```

   * Reads all `*.txt` files in `~/Downloads/Permissions`
   * Constructs and saves `permission_matrix.npy`

3. **Train Machine Learning Model**

   ```bash
   python train_ml_model.py
   ```

   * Loads `permission_matrix.npy`
   * Uses a predefined label array for 10 APK samples (1=malicious, 0=benign)
   * Trains a Random Forest classifier and saves it as `trained_model.pkl`

4. **Test on New APKs**

   ```bash
   python test_ml_model.py
   ```

   * Points to `~/Downloads/NEWAPK` for analysis
   * Loads `trained_model.pkl`
   * Outputs a permission matrix and classification results for each APK

## File Details

### `extract_permissions_log.py`

* Imports APK parser from Androguard
* Iterates over APK files and extracts permissions
* Writes permission lists to individual `.txt` files

### `permission_matrix.py`

* Reads permission text files
* Maps a master list of 10 permissions to binary features
* Outputs a NumPy matrix for ML training

### `train_ml_model.py`

* Loads the permission matrix and manual labels
* Splits data into train/test sets
* Trains and evaluates a Random Forest classifier
* Saves the trained model

### `test_ml_model.py`

* Loads the trained model and master permissions
* Extracts permissions from new APKs
* Constructs test feature rows
* Predicts and prints whether each APK is malicious or benign

## Configuration

If your APK or output directories differ from the defaults (`~/Downloads/APKs`, `~/Downloads/Permissions`, `~/Downloads/NEWAPK`), edit the corresponding path variables in each script.

## Contributing

Contributions, bug reports, and feature requests are welcome. Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
