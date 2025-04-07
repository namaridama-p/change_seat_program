import csv
import numpy as np

def main():
    data = inputs()
    seeds = int(input("seed(-1はランダム): "))
    if seeds == -1:
        seeds = None
    seat = Shuffle(data, seeds)
    ans = static_seat_change(seat)
    printer(ans)
    output(ans)

def Shuffle(data, seed=None):
    if seed is not None:
        rng = np.random.default_rng(seed)
    else:
        rng = np.random.default_rng()
    rng.shuffle(data)
    data.insert(0, 0)
    data.insert(1, 0)
    data.insert(4, 0)
    return data

def static_seat_change(seat):
    static_seat = input_static_seat()
    for data in static_seat:
        student_num = data[0]
        seat_num = data[1]
        before_seat = 0
        before_index = seat.index(student_num)
        before_seat = seat[seat_num]
        print("before_index", before_index)
        print("before_seat", before_seat)
        seat[seat_num] = student_num
        seat[before_index] = before_seat
    return seat

def printer(seat):
    for i in range(len(seat)):
        if i % 5 == 0:
            print()
        if seat[i] == 0:
            print("\t", end="")
        if seat[i] != 0:
            print(seat[i], end="\t")

def static_change(seat):
    pass
def output(seat):
    a = [[] for i in range(len(seat)//5 )]
    with open("output/output.csv", "w") as f:
        writer = csv.writer(f, lineterminator="\n")
        count = 0
        for i in range(len(seat)):
            if i % 5 == 0 and i != 0:
                count += 1
            if seat[i] == 0:
                a[count].append("")
            else:
                a[count].append(seat[i])
        writer.writerows(a,)

def inputs():
    with open("input/input.csv", "r") as f:
        data = [int(i[0]) for i in list(csv.reader(f))]
        print(list(data))
    return data

def input_static_seat():
    with open("input/static_seat.csv", "r") as f:
        data = [[int(i[0]),int((int(i[1]) * 5 )+ int(i[2]))] for i in list(csv.reader(f))]
        print(list(data))
    return data
if __name__ == "__main__":
    main()