import numpy as np
def process_messages(model, messages, tools_list, num_tools, n_embd, n_features, n_samples, normalize=False):
    """
    messages: list[str] length n_samples
    
    Returns:
        X: np.array shape (n_samples, n_embd)
        Q: np.array shape (n_samples, n_features)
    """
    
    
    
    # ---- Preallocate arrays ----
    X = np.zeros((n_samples, n_embd+n_features), dtype=np.float32)
    Q = np.zeros((n_samples, n_features), dtype=np.float32)
    
    
    # ---- Loop through remaining messages ----
    for i in range(n_samples):
        #X[i] = gen_vector(model, messages[i], tools_list[i], num_tools[i])
        X[i] = cactus_embed(model, messages[i], normalize=normalize)
        local = generate_cactus([messages[i]], [tools_list[i]])
        extra_features = [num_tools[i]/7.0, local["confidence"]]
        Q[i] = message_to_features(messages[i], extra_features)
    
    return X, Q

def gen_vector(model, msg, tools, num_tools, normalize=False):
    embd = cactus_embed(model, msg, normalize=normalize)
    local = generate_cactus(transform_msg(msg), tools)
    extra_features = [num_tools/7.0, local["confidence"]]
    return message_to_features(msg, extra_features)

def transform_msg(msg):
    return [{"role": "user", "content": msg}]

import re

def message_to_features(message, extra_features):
    """
    message: str
    extra_features: list[float/int]  -> appended at end
    keyword_list: list[str]
    
    Returns:
        list of features
    """
    keyword_list=["weather", "alarm", "message", "reminder", "contacts", "music"]
    if not message:
        base_features = [0.0] * 8
        return base_features + list(extra_features)
    
    # Lowercase for consistency
    msg = message.lower()
    
    # -----------------------------
    # 1️Token-level features
    # -----------------------------
    tokens = msg.split()
    num_tokens = len(tokens)/30.0
    
    avg_word_length = (
        sum(len(word.strip(",.!?;:")) for word in tokens) / num_tokens
        if num_tokens > 0 else 0.0
    )
    
    # -----------------------------
    # 2️Count punctuation/connectors
    # -----------------------------
    num_commas = msg.count(",")/5.0
    num_periods = msg.count(".")/5.0
    
    # count standalone "and"
    num_ands = len(re.findall(r"\band\b", msg))/5.0
    
    # -----------------------------
    # 3️Clause splitting
    # Split by:
    #   ", and"
    #   ","
    #   "."
    #   standalone "and"
    # -----------------------------
    clause_splits = re.split(r",\s*and\s*|,\s*|\.\s*|\band\b", msg)
    clauses = [c.strip() for c in clause_splits if c.strip()]
    
    num_clauses = len(clauses) if clauses else 1
    
    avg_clause_length = (
        sum(len(c.split()) for c in clauses) / num_clauses
        if num_clauses > 0 else 0.0
    )
    
    # -----------------------------
    # 4️Keyword features
    # -----------------------------
    keyword_set = set(k.lower() for k in keyword_list)
    
    num_keywords = sum(
        1 for token in tokens
        if token.strip(",.!?;:") in keyword_set
    )/3.0
    
    avg_keywords_per_clause = (
        num_keywords / num_clauses
        if num_clauses > 0 else 0.0
    )
    
    # -----------------------------
    # Combine all features
    # -----------------------------
    base_features = [
        num_tokens,
        avg_word_length,
        num_commas,
        num_ands,
        num_periods,
        avg_clause_length,
        num_keywords,
        avg_keywords_per_clause
    ]
    
    return base_features + list(extra_features)