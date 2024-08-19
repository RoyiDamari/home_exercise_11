# Exercise 1
# a
number: tuple[int] = (99,);

# b
num_tup: tuple[int] = (77, 88, 99);

# c
tup: tuple[int] = (10, 20, 30, 40, 50);


def len_tup(tup: tuple[int]) -> int:
    return len(tup);


print(len_tup(tup));

# d
tup1: tuple[str] = ("I", "Love", "To", "Program", "Python");
tup2: tuple[int] = (60, 70, 80, 90, 100);


def concat_tup(t1: tuple[str], t2: tuple[any]) -> tuple[any]:
    return t1 + t2;


print(concat_tup(tup1, tup2));

# e - first way
tup_1: tuple[int] = (60, 70, 80, 90, 100);
tup_2: tuple[int] = (30, 70, 50, 90, 10);
print(tuple(x for x in tup_1 if x in tup_2));


# e - second way
def common_numbers(t1: tuple[int], t2: tuple[int]) -> tuple[int]:
    my_list: list[int] = [];
    for t in t1:
        if t in t2:
            my_list.append(t);
    return tuple(my_list);


print(common_numbers(tup_1, tup_2));

# f
print(tuple(x for x in tup_1 if x not in tup_2) + tuple(x for x in tup_2 if x not in tup_1));

# g
my_tup: tuple[any] = (10, "ID", 30, "Street",50);


def tup_index(t: tuple[any], index: int) -> tuple[any] | None:
    try:
        return t[index];
    except IndexError:
        return None


print(tup_index(my_tup, 3));

# h
my_tup: tuple[any] = (10, "ID", 30, "Street",50);


def tup_reverse(t: tuple[any]) -> tuple[any]:
    return tuple(list(t[::-1]));


print(tup_reverse(my_tup));

# i
my_tup: tuple[int] = (10, 8, 5, 5, 3, 2, 50, 10, 30, 40);


def tup_div(tup: tuple[int], index: int) -> tuple[int]:
    return len([t for t in tup if t % index == 0]);


print(tup_div(my_tup, 10));

# j
my_tup: tuple[any] = (10, "ID", 30, "Street",50);


def tup_dup(t: tuple[any], index: int) -> tuple[any] | None:
    return my_tup * index;


print(tup_dup(my_tup, 3));

# k
my_tup: tuple[any] = (10, "ID", 30, "Street", 50);


def tup_split(t: tuple[any]) -> tuple[any]:
    return tuple((index, item) for index, item in enumerate(my_tup));


print(tup_split(my_tup));

# l
import statistics
my_tup: tuple[int] = (10, 8, 5, 5, 3, 2, 50, 10, 30, 40);


def tuple_analysis(t: tuple[int]) -> dict[int]:
    max_value: int = max(t);
    min_value: int = min(t);
    average_value: float = statistics.mean(t);
    count: int = len(t);
    sorted_desc: tuple[int] = tuple(sorted(t, reverse=True));
    sorted_asc: tuple[int] = tuple(sorted(t));

    frequency = {};
    for num in t:
        if num in frequency:
            frequency[num] += 1;
        else:
            frequency[num] = 1;

    analysis = {
        "Maximum": max_value,
        "Minimum": min_value,
        "Average": average_value,
        "Count": count,
        "Sorted Descending": sorted_desc,
        "Sorted Ascending": sorted_asc,
        "Frequency": frequency
    };

    return analysis


print(tuple_analysis(my_tup));

# m
my_tup: tuple[str] = ('H', 'e', 'l', 'l', 'o');


def make_string_of_tuple(t: tuple[str]) -> str:
    return ''.join(t)


print(make_string_of_tuple(my_tup));

# n
word: str = "Hello";


def make_tuple_of_string(t: str) -> tuple[str]:
    return tuple(t);


print(make_tuple_of_string(word));

# o
my_tup: tuple[int] = (10, 8, 5, 5, 3, 2, 50, 10, 30, 40);


def remove_number(t: tuple[int], number: int) -> tuple[int]:
    return tuple(i for i in t if i != number);


print(remove_number(my_tup, 10));

# p
my_tup: tuple[any] = (10, 8, 5, 5, 'Love', 2, 50, 50, 30, 'Love');


def remove_duplicate(t: tuple[any]) -> tuple[any]:
    my_list: any = [];
    for i in t:
        if i not in my_list:
            my_list.append(i);

    return tuple(my_list);


print(remove_duplicate(my_tup));

# q
my_tup: tuple[int] = (10, 8, 5, 5, 3, 2, 5, 10, 30, 40);


def check_number_index(t: tuple[int], index: int) -> tuple[int]:
    return tuple(i for i, x in enumerate(t) if x == index);


print(check_number_index(my_tup, 5));

# r
names: list[str] = [];
grades: list[int] = [];

while True:
    try:
        name: str = input("Please enter a name (type 'done' to finish): ");
        if name.lower() == "done":
            break

        if any(char.isdigit() for char in name):
            raise ValueError("Names cannot contain numbers. Please enter a valid name.");
        else:
            print(f"Valid name entered: {name}")
            names.append(name);

    except ValueError as e:
        print(e);


while True:
    try:
        grade: int = int(input("Please enter a grade (type '-999' to finish): "));
        if grade == -999:
            break
        else:
            grades.append(grade);

    except Exception as e:
        print(f"Something went wrong ---{e}---...try again");

print(tuple(zip(names, grades)));

# Exercise 2
'''The difference is that list can be modified,
 which mean you can change add and delete values while in tuple you cannot make any changes'''

'''If you have data that you don't want to make any changes to and keep it constant,
it would be better to use a tuple, otherwise it would be better to use a list'''

# Exercise 3
'''A dictionary can be changed even though the tuple itself cannot be changed,
 therefore since the dictionary is an element within the tuple then it can be done'''