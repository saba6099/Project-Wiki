import heapq


class Merger():
    def __init__(self):
        try:
            # 1. create priority queue
            self._heap = []
            self._output_file = open('finalIndex', 'w+')

        except:
            print("Error while creating Merger:")

    def merge(self, input_files):
        # try:
        # open all files
        open_files = []
        for file__ in input_files:
            open_files.append(open(file__, 'r'))
            # print(open_files)
        for file__ in open_files:
            p1 = (file__.readline())
            # print(p1)
            heapq.heappush(self._heap, (p1, file__))

        while (self._heap):
            # get the smallest key
            # smallest = heapq.heappop(self._heap)
            smallest = heapq.heappop(self._heap)
            smaller = heapq.heappop(self._heap)
            # print(smallest, "*")
            term1, postings1 = smallest[0].split('|')
            term2, postings2 = smaller[0].split('|')
            print("smallest=", term1)
            print("smaller=", term2)
            # print("#",smaller, "#")
            #   f = open(self.indexFile, 'r');
            if term1 == term2:
                #print("equal")

                postings1 = postings1.strip()
                postings2 = postings2.strip()
                trm = term1 + "|" + postings1 + ";" + postings2+"\n"
                self._output_file.write(trm)
                read_line = (smallest[1].readline())
                if (len(read_line) != 0):
                    #print("pushed", read_line)
                    heapq.heappush(self._heap, ((read_line), smallest[1]))
                else:
                    print("file1 finished")
                    #read_line = heapq.heappop(self._heap)
                    #self._output_file.write(read_line[0])
                    read_line = (smaller[1].readline())
                    while (len(read_line) != 0):
                        self._output_file.write(read_line)
                        read_line = (smaller[1].readline())
                read_line = (smaller[1].readline())
                if (len(read_line) != 0):
                    #print("pushed", read_line)
                    heapq.heappush(self._heap, ((read_line), smaller[1]))
                if (len(read_line) == 0):
                    print("file2 finished")
                    #read_line = heapq.heappop(self._heap)
                    #self._output_file.write(read_line[0])
                    read_line = (smallest[1].readline())
                    while (len(read_line) != 0):
                        self._output_file.write(read_line)
                        read_line = (smallest[1].readline())


            else:
                # read_line = (smaller[1].readline())
                #print("pushed smaller:", str(smaller[0]))
                heapq.heappush(self._heap, (str(smaller[0]), smaller[1]))
                postings1 = postings1.strip()
                trm = term1 + "|" + postings1 + "\n"
                self._output_file.write(trm)
                read_line = (smallest[1].readline())
                #print("next of smallest=", read_line)
                ##print('#',read_line,'#')
                # check that this file has not ended
                ##print(smallest[1])
                if (len(read_line) != 0):
                    #print(" pushed", read_line)
                    heapq.heappush(self._heap, ((read_line), smallest[1]))
                if (len(read_line) == 0):
                    #print("a file finished")
                    read_line = heapq.heappop(self._heap)
                    self._output_file.write(read_line[0])
                    read_line = (smaller[1].readline())
                    while (len(read_line) != 0):
                        #print("hey")
                        self._output_file.write(read_line)
                        #print("popped n written", read_line)
                        #smaller = heapq.heappop(self._heap)
                        #self._output_file.write(read_line)
                        read_line = (smaller[1].readline())
        # clean up
        [file__.close() for file__ in open_files]
        self._output_file.close()

        # except :
        #    print("Error while merging: ")

    def _delimiter_value(self):
        return "\n"


def test():

    files = ['Mergeee1', 'Mergeee2']
    merger = Merger()
    merger.merge(files)


if __name__ == '__main__':
    test()