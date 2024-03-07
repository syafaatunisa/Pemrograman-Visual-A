my_set = set()

my_set.add(1)
my_set.add(2)
my_set.add(3)

print("Set awal:", my_set)

my_set.remove(2)

print("Set setelah dihapus:", my_set)

print("Jumlah elemen dalam set:", len(my_set))

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
print("Gabungan set:", union_set)

intersection_set = set1.intersection(set2)
print("Irisan set:", intersection_set)

difference_set = set1.difference(set2)
print("Selisih set:", difference_set)

subset = {1, 2}.issubset(set1)
superset = set1.issuperset({1, 2})
print("Subset:", subset)
print("Superset:", superset)
