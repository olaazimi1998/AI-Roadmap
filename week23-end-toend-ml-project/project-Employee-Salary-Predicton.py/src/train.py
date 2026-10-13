from preprocessing import MODEL_PATH, train_and_evaluate


if __name__ == "__main__":
    _, metrics = train_and_evaluate()

    print("MAE:", metrics["mae"])
    print("RMSE:", metrics["rmse"])
    print("R²:", metrics["r2"])
    print(f"Model saved to: {MODEL_PATH}")
