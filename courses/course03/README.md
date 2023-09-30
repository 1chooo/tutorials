# Week03 - 2023-1008

print(), string(), split(), for

### 上週回顧
- [ ] `input()`


### `float()` 取位數補充

#### 透過型別轉換
另外我們也可以透過先前學習到的型別轉換先轉換成 `str`，再透過對 `str` 的處理轉換成 `float` 因而得到我們想要的數值。

```py
probability = 0.123456789
probability_str = str(probability)
probability_str = probability_str[:4]
probability = float(probability_str)
print(probability)      # 0.12
```

#### 透過運算的方式截斷
將一個浮點數 `probability` 乘以 100，然後再將結果轉換為整數。接著，它會再將該整數轉換回浮點數，並保留兩位小數。這樣的處理方式通常稱為「四捨五入到兩位小數」。

這樣的處理方式可能有助於限制浮點數的小數部分，以確保它只保留兩位小數，而不進行四捨五入

```py
probability = 0.123456789
print(int(probability * 100) / 100)
```