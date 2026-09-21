# SVM and KNN Digit Classification

A small machine-learning project that classifies handwritten digits from scikit-learn's `digits` dataset using two supervised learning algorithms:

- Support Vector Machine (SVM) with an RBF kernel
- K-Nearest Neighbors (KNN) with 3 neighbors

The notebook trains both models, compares their accuracy and classification reports, visualizes sample handwritten digits, and tests both models on one held-out image.

## Dataset

The project uses the built-in `load_digits` dataset:

- 1,797 handwritten digit images
- 10 classes: digits `0` through `9`
- 64 features per image, representing an `8 x 8` pixel grid
- 80% training data and 20% test data
- Reproducible split with `random_state=42`

## Requirements

```bash
pip install scikit-learn matplotlib pandas
```

## Run the Notebook

Open `project-svm & knn .ipynb` in VS Code or Jupyter and run the cells from top to bottom.

The notebook will:

1. Load and inspect the digit dataset.
2. Split the data into training and testing sets.
3. Train and evaluate the SVM model.
4. Train and evaluate the KNN model.
5. Compare both model accuracies.
6. Display a styled gallery of handwritten digits.
7. Predict one held-out image with both models.

## Visualization

The Matplotlib chart presents ten sample digit images in a two-row gallery with a high-contrast `magma` color map. The figure also displays the final SVM and KNN accuracy values so the visual output connects directly to the model comparison.

## Expected Result

Both models should achieve strong performance on this dataset. Exact accuracy can vary slightly if the split or model parameters are changed. The final prediction cell reports the actual label and the prediction from each model for the same test image.

## Project Structure

```text
week17/day3/
├── project-svm & knn .ipynb
└── README.md
```
