#1
def evaluate_classification_model(tp, fp, fn):
   
    if not isinstance(tp, int):
        print('tp must be int')
        return
    if not isinstance(fp, int):
        print('fp must be int')
        return
    if not isinstance(fn, int):
        print('fn must be int')
        return
 
    if tp <= 0 or fp <= 0 or fn <= 0:
        print('tp and fp and fn must be greater than zero')
        return
    
   
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
   
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1-Score: {f1_score:.4f}')

evaluate_classification_model(2, 4, 5)




#2
import math
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

# Các function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    return x if x >= 0 else alpha * (math.exp(x) - 1)


def apply_activation_function(x, activation_name):
    
    if not is_number(x):
        print('x must be a number')
        return
    
   
    if activation_name not in ['sigmoid', 'relu', 'elu']:
        print(f'{activation_name} is not supported')
        return
    
   
    x = float(x)
    if activation_name == 'sigmoid':
        result = sigmoid(x)
    elif activation_name == 'relu':
        result = relu(x)
    elif activation_name == 'elu':
        result = elu(x, alpha=0.01)
    
    print(f'The result of {activation_name}({x}) is {result:.4f}')

apply_activation_function('10', 'sigmoid')
apply_activation_function('-10', 'sigmoid')
apply_activation_function('-10', 'relu')
apply_activation_function('10', 'relu')
apply_activation_function('10', 'elu')
apply_activation_function('-10', 'elu')
apply_activation_function('abc', 'sigmoid')  
apply_activation_function('10', 'belu')  




#3
import random
import math
def calculate_loss(num_samples, loss_name):
   
    if not num_samples.isnumeric():
        print('number of samples must be an integer number')
        return
    
    num_samples = int(num_samples)
    
    predicts = []
    targets = []
  
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        predicts.append(predict)
        targets.append(target)
        print(f'sample-{i}, predict: {predict:.2f}, target: {target:.2f}')
    
    if loss_name == 'MAE':
        loss = sum(abs(p - t) for p, t in zip(predicts, targets)) / num_samples
    elif loss_name == 'MSE':
        loss = sum((p - t) ** 2 for p, t in zip(predicts, targets)) / num_samples
    elif loss_name == 'RMSE':
        loss = math.sqrt(sum((p - t) ** 2 for p, t in zip(predicts, targets)) / num_samples)
  
    print(f'Loss name: {loss_name}')
    print(f'Loss: {loss:.4f}')

num_samples = input('Enter the number of samples: ')
loss_name = input('Enter the loss function name (MAE, MSE, RMSE): ')
calculate_loss(num_samples, loss_name)




#4
import math
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def approximate_sin(x, n):
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        result += term
    return result


def approximate_cos(x, n):
    result = 0
    for i in range(n):
        coef = (-1) ** i
        term = coef * (x ** (2 * i)) / factorial(2 * i)
        result += term
    return result


def approximate_sinh(x, n):
    result = 0
    for i in range(n):
        term = x ** (2 * i + 1) / factorial(2 * i + 1)
        result += term
    return result

def approximate_cosh(x, n):
    result = 0
    for i in range(n):
        term = x ** (2 * i) / factorial(2 * i)
        result += term
    return result


def test():
    x = float(input("Enter the value of x in radians: "))
    n = int(input("Enter the number of iterations (n): "))

    sin_x = approximate_sin(x, n)
    cos_x = approximate_cos(x, n)
    sinh_x = approximate_sinh(x, n)
    cosh_x = approximate_cosh(x, n)
    
    # In ra kết quả
    print(f"sin({x}) ≈ {sin_x}")
    print(f"cos({x}) ≈ {cos_x}")
    print(f"sinh({x}) ≈ {sinh_x}")
    print(f"cosh({x}) ≈ {cosh_x}")

# Gọi hàm test() để kiểm tra
test()





