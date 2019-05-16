import heapq


class Merger():
    def __init__(self):
        try:
            # 1. create priority queue
            self._heap = []
            self._output_file = open('Merge', 'w+')

        except:
            print("Error while creating Merger:")
    def writetofile(self,small1,small2):
        term1, postings1 = small1[0].split('|')
        term2, postings2 = small2[0].split('|')
        postings1 = postings1.strip()
        postings1 = postings1.strip()
        trm = term1 + "|" + postings1 + ";" + postings2+"\n"
        self._output_file.write(trm)
        read_line = (small1[1].readline())
        if (len(read_line) != 0):
            print("pushed", read_line)
            heapq.heappush(self._heap, ((read_line), small1[1]))
        read_line = (small2[1].readline())
        if (len(read_line) != 0):
            print("pushed", read_line)
            heapq.heappush(self._heap, ((read_line), small2[1]))

    def merge(self, input_files):
        # try:
        # open all files
        open_files = []
        for file__ in input_files:
            open_files.append(open(file__, 'r'))
            # print(open_files)

        # 2. Iterate through each file f
        # enqueue the pair (nextNumberIn(f), f) using the first value as priority key
        for file__ in open_files:
            p1 = (file__.readline())
            # print(p1)
            heapq.heappush(self._heap, (p1, file__))

        while (self._heap):
            # get the smallest key
            # smallest = heapq.heappop(self._heap)
            smallest = heapq.heappop(self._heap)
            smaller = heapq.heappop(self._heap)
            small = heapq.heappop(self._heap)
            # print(smallest, "*")
            term1, postings1 = smallest[0].split('|')
            term2, postings2 = smaller[0].split('|')
            term3, postings3 = smaller[0].split('|')
            print("smallest=", term1)
            print("smaller=", term2)
            print("small=", term3)
            # print("#",smaller, "#")
            #   f = open(self.indexFile, 'r');

            if term1 == term2==term3:
                print("true")

                postings1 = postings1.strip()
                postings2 = postings2.strip()
                postings3 = postings3.strip()
                trm = term1 + "|" + postings1 + ";" + postings2 + ";" + postings3+"\n"
                # print("*",trm,"*")
                self._output_file.write(trm)
                read_line = (smallest[1].readline())
                if (len(read_line) != 0):
                    print("pushed smallest", read_line)
                    heapq.heappush(self._heap, ((read_line), smallest[1]))
                read_line = (smaller[1].readline())
                if (len(read_line) != 0):
                    print("pushed smaller", read_line)
                    heapq.heappush(self._heap, ((read_line), smaller[1]))
                    read_line = (small[1].readline())
                if (len(read_line) != 0):
                    print("pushed small", read_line)
                    heapq.heappush(self._heap, ((read_line), small[1]))
            elif term1==term2:
                print("two equal")

                postings1 = postings1.strip()
                postings2 = postings2.strip()
                trm = term1 + "|" + postings2 + ";" + postings1 + "\n"
                self._output_file.write(trm)
                read_line = (smallest[1].readline())
                if (len(read_line) != 0):
                    # print("pushed", read_line)
                    heapq.heappush(self._heap, ((read_line), smallest[1]))
                read_line = (smaller[1].readline())
                if (len(read_line) != 0):
                    # print("pushed", read_line)
                    heapq.heappush(self._heap, ((read_line), smaller[1]))
                heapq.heappush(self._heap, (str(smallest[0]), smallest[1]))
            else:
                # read_line = (smaller[1].readline())
                print("pushed", str(smaller[0]))
                heapq.heappush(self._heap, (str(smaller[0]), smaller[1]))

                print("pushed", str(small[0]))
                heapq.heappush(self._heap, (str(small[0]), small[1]))

                trm = term1 + "|" + postings1+"\n"
                self._output_file.write(trm)
                read_line = (smallest[1].readline())
                print("next of smallest=", read_line)
                ##print('#',read_line,'#')
                # check that this file has not ended
                ##print(smallest[1])
                if (len(read_line) != 0):
                    print(" pushed", read_line)
                    heapq.heappush(self._heap, ((read_line), smallest[1]))

        # clean up
        [file__.close() for file__ in open_files]
        self._output_file.close()

        # except :
        #    print("Error while merging: ")

    def _delimiter_value(self):
        return "\n"


def test():
    files = ['heap1', 'heap2', 'heap3']
    merger = Merger()
    merger.merge(files)


if __name__ == '__main__':
    test()