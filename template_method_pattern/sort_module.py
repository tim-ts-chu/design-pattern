


class QuickSort:
    def __init__(self):
        self._compare_method = None

    def setCompareMethod(self, compare_method):
        self._compare_method = compare_method

    def sort(self, objects):
        if (len(objects) < 2):
            return objects

        self._qsort(objects, 0, len(objects)-1)
        return objects

    def _qsort(self, objects, l, r):
        if r == l:
            return
        if r - l == 1:
            if self._compare_method(objects[l], objects[r]):
                self._swap(objects, l, r)
        else:
            lmark = l + 1
            rmark = r
            while lmark != rmark:
                if self._compare_method(objects[lmark], objects[l]):
                    # lmark > pivot
                    while lmark != rmark:
                        if not self._compare_method(objects[rmark], objects[l]):
                            # rmark < pivot
                            self._swap(objects, lmark, rmark)
                            lmark = lmark + 1
                        else:
                            rmark =  rmark - 1
                else:
                    lmark = lmark + 1

            if self._compare_method(objects[lmark], objects[l]):
                # lmark > l
                new_pivot = lmark-1
            else:
                # lmark < l
                new_pivot = lmark

            self._swap(objects, l, new_pivot)
            if new_pivot-1 > l:
                self._qsort(objects, l, new_pivot-1)
            if new_pivot+1 < r:
                self._qsort(objects, new_pivot+1, r)

    def _swap(self, objects, idx1, idx2):
        t = objects[idx1]
        objects[idx1] = objects[idx2]
        objects[idx2] = t


