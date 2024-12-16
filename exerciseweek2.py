#1
def max_in_sliding_window(num_list, k):
    if not num_list or k <= 0:
        return []
    max_values = []
    for i in range(len(num_list) - k + 1):
        window_max = max(num_list[i:i + k])
        max_values.append(window_max)

    return max_values

#test
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 2
print(max_in_sliding_window(num_list, k))


#2
def charNumber(string):
    char_count = {}
    for char in string:
        char= char.lower();
        if char in char_count:
           char_count[char] += 1
        else:
           char_count[char]=1
    return char_count

#test
string1 = 'Happiness'
print(charNumber(string1)) 
string2 = 'smiles'
print(charNumber(string2))


#3
def word_count(file_path):
    word_count_dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.lower().split()
            for word in words:
                if word in word_count_dict:
                    word_count_dict[word] += 1
                else:
                    word_count_dict[word] = 1
    
    return word_count_dict

#test
file_path = 'P1_data.txt'
print(word_count(file_path))



#4
def levenshtein_distance(S, T):
    m, n = len(S), len(T)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
   
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i - 1] == T[j - 1]:
                cost = 0
            else:
                cost = 1
            dp[i][j] = min(dp[i - 1][j] + 1,    
                           dp[i][j - 1] + 1,      
                           dp[i - 1][j - 1] + cost)  
   
    return dp[m][j]

#test
S = "Le Tu Trung"
T = "Minh Kien"
print(levenshtein_distance(S, T))  



