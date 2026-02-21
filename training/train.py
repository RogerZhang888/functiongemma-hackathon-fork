import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import HistGradientBoostingClassifier, HistGradientBoostingRegressor
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, mean_squared_error


# ------------------------------------------------------------
# Inputs (given):
#   p: (n_samples, n_embd)     embeddings
#   q: (n_samples, n_features) tabular features
#   y: (n_samples, 1) or (n_samples,) labels/targets
# ------------------------------------------------------------

def train_router_gbdt(p, q, y, *, pca_dim=32, test_size=0.2, seed=42, task="regression"):
    """
    task: "classification" (y in {0,1}) or "regression" (continuous)
    Returns trained model + preprocessors + val metrics.
    """

    # --- Basic shape cleanup ---
    p = np.asarray(p)
    q = np.asarray(q)
    y = np.asarray(y).reshape(-1)  # (n_samples,)

    assert p.shape[0] == q.shape[0] == y.shape[0], "p, q, y must have same n_samples"

    # --- 1) Train/Val split (keep indices aligned across p, q, y) ---
    stratify = y if (task == "classification" and len(np.unique(y)) <= 20) else None
    p_tr, p_va, q_tr, q_va, y_tr, y_va = train_test_split(
        p, q, y,
        test_size=test_size,
        random_state=seed,
        stratify=stratify,
    )

    # --- 2) PCA on p (fit ONLY on train), concat with q ---
    # Standardize embeddings before PCA (safe default; remove if you know embeddings are already standardized)
    p_scaler = StandardScaler(with_mean=True, with_std=True)
    p_tr_scaled = p_scaler.fit_transform(p_tr)
    p_va_scaled = p_scaler.transform(p_va)

    pca = PCA(n_components=pca_dim, random_state=seed)
    p_tr_pca = pca.fit_transform(p_tr_scaled)
    p_va_pca = pca.transform(p_va_scaled)

    X_tr = np.concatenate([q_tr, p_tr_pca], axis=1)
    X_va = np.concatenate([q_va, p_va_pca], axis=1)

    # --- 3) Train a GBDT on X -> y ---
    if task == "classification":
        model = HistGradientBoostingClassifier(
            learning_rate=0.1,
            max_depth=None,
            max_iter=300,
            random_state=seed,
        )
        model.fit(X_tr, y_tr)

        y_pred = model.predict(X_va)
        metrics = {
            "val_accuracy": float(accuracy_score(y_va, y_pred)),
            "val_f1": float(f1_score(y_va, y_pred, zero_division=0)),
        }
        # AUC only if binary and model supports predict_proba
        if len(np.unique(y_va)) == 2 and hasattr(model, "predict_proba"):
            y_prob = model.predict_proba(X_va)[:, 1]
            metrics["val_auc"] = float(roc_auc_score(y_va, y_prob))

    elif task == "regression":
        model = HistGradientBoostingRegressor(
            learning_rate=0.1,
            max_depth=None,
            max_iter=300,
            random_state=seed,
        )
        model.fit(X_tr, y_tr)

        y_pred = model.predict(X_va)
        metrics = {
            "val_rmse": float(np.sqrt(mean_squared_error(y_va, y_pred))),
            "val_mse": float(mean_squared_error(y_va, y_pred)),
        }
    else:
        raise ValueError("task must be 'classification' or 'regression'")

    bundle = {
        "model": model,
        "p_scaler": p_scaler,
        "pca": pca,
        "pca_dim": pca_dim,
        "metrics": metrics,
        "explained_variance_sum": float(pca.explained_variance_ratio_.sum()),
    }
    return bundle


# -------------------------------
# Example usage:
# -------------------------------
# bundle = train_router_gbdt(p, q, y, pca_dim=32, task="classification")
# print(bundle["metrics"])
# print("PCA explained variance:", bundle["explained_variance_sum"])




