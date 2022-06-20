from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'index.html')


def input(request):
    print("hello")

    all_a = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6']
    all_b = ['b1', 'b2', 'b3', 'b4', 'b5', 'b6']
    val = []
    wt = []
    for var in all_a:
        temp = request.GET.get(var)
        if temp == '' or temp is None:
            temp = 0
        else:
            temp = int(temp)

        val.append(temp)

    for var in all_b:
        temp = request.GET.get(var)
        if temp == '' or temp is None:
            temp = 0
        else:
            temp = int(temp)

        wt.append(temp)

    capacity = int(request.GET.get('capacity'))

    explanation, maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    return render(request, 'output.html', {'result': maxValue, "explanation": explanation})


class ItemValue:

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val // wt

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapSack:
    @staticmethod
    def getMaxValue(wt, val, capacity):
        explanation = []
        iVal = []
        for i in range(len(wt)):
            if wt[i] != 0:
                iVal.append(ItemValue(wt[i], val[i], i))

        # sorting items by value
        iVal.sort(reverse=True)

        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity = capacity - curWt
                totalValue = totalValue + curVal
                explanation.append(f"{curWt} kg item is taken with a weight of -  {curWt} kg")
                explanation.append(f"which gives us value - {curVal} Rs")
            else:
                fraction = capacity / curWt
                value = curVal * fraction
                totalValue = totalValue + value
                explanation.append(f"{curWt} kg item is taken with a weight of -  {fraction * curWt}  kg")
                explanation.append(f"which gives us a value -  {value} Rs")
                capacity = int(capacity - (curWt * fraction))
                break
        return explanation, totalValue


if __name__ == "__main__":
    a1 = int(input("enter 1st value"))
    a2 = int(input("enter 2nd value"))
    a3 = int(input("enter 3rd value"))
    a4 = int(input("enter 4th value"))
    a5 = int(input("enter 5th value"))
    a6 = int(input("enter 6th value"))
    b1 = int(input("enter 1st weight"))
    b2 = int(input("enter 2st weight"))
    b3 = int(input("enter 3rd weight"))
    b4 = int(input("enter 4th weight"))
    b5 = int(input("enter 5th weight"))
    b6 = int(input("enter 6th weight"))
    val = [a1, a2, a3, a4, a5, a6]
    wt = [b1, b2, b3, b4, b5, b6]
    capacity = int(input("enter the capacity- "))

    explanation, maxValue = FractionalKnapSack.getMaxValue(wt, val, capacity)
    print("Maximum value in Knapsack =", maxValue, "Rs")