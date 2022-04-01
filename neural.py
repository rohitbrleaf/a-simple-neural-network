
inputs = [1,2,3,4,5]
targtes = [10,20,30,40,50]

weight = 0.1
learning_depth = 0.1

def predict(i):
    return i * weight


for _ in range(25):
    predicted = [ predict(i) for i in inputs]
    errors = [ t-p for t,p in zip(targtes,predicted)]
    cost = sum(errors)/len(targtes)
    print(f"weight:{weight:.2f} and cost:{cost:.2f}")
    weight += cost * learning_depth

inputss = [6,7]

predict_value = [ predict(i) for i in inputss]

for i in predict_value:
    print(round(i))


