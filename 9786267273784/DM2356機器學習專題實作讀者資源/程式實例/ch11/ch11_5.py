# ch11_5.py
# 先驗機率
P_A = 0.01                  # 有疾病的機率
P_B_given_A = 0.99          # 有疾病的情況下，測試為陽性的機率
P_A_prime = 1 - P_A         # 沒有疾病的機率
P_B_given_A_prime = 0.01    # 沒有疾病的情況下，測試為陽性的機率

# 計算總的陽性機率
P_B = P_B_given_A * P_A + P_B_given_A_prime * P_A_prime

# 應用貝氏定理
P_A_given_B = (P_B_given_A * P_A) / P_B

print("在測試為陽性的情況下，真的有疾病的機率是：", P_A_given_B)


