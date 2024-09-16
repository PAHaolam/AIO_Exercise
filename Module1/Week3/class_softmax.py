import torch


class Softmax(torch.nn.Module):
    def forward(self, data):
        exp_data = torch.exp(data)
        sum_exp_data = sum(exp_data)
        exp_data = exp_data/sum_exp_data
        return exp_data


class SoftmaxStable(torch.nn.Module):
    def forward(self, data):
        c = max(data)
        exp_data = torch.exp(data-c)
        sum_exp_data = sum(exp_data)
        exp_data = exp_data/sum_exp_data
        return exp_data


data = torch.Tensor([1, 2, 3])
softmax = Softmax()
output = softmax(data)
print(f"Softmax output = {output}")

softmax_stable = SoftmaxStable()
output2 = softmax_stable(data)
print(f"Softmax stable output = {output2}")
