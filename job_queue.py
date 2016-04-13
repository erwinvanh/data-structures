# python2
import Queue as Q

class JobQueue:
    def __init__(self):
        self.assigned_workers = Q.PriorityQueue()
        self.start_times = Q.PriorityQueue()

    def read_data(self):
        self.num_workers, m = map(int, raw_input().split())
        self.jobs = list(map(int, raw_input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        #for i in range(len(self.jobs)):
        #  print self.start_times[i]
        while not self.start_times.empty():
            line = self.start_times.get()
            print line[1], line[0]

    def assign_jobs(self):
        # Fill the PriorityQueue for assigned_workers
        for i in range(self.num_workers):
            self.assigned_workers.put(( 0, i))

        next_free_time = [0] * self.num_workers
        for i in range(len(self.jobs)):
          next_worker = self.assigned_workers.get()
          # Faster solution : print it right now (don't use start_times)
          print next_worker[1], next_worker[0]
          #self.start_times.put ((next_worker[0], next_worker[1]))
          # Plact it back on the queue with the endtime as PriorityQueue
          endtime = next_worker[0] + self.jobs[i]
          self.assigned_workers.put(( endtime, next_worker[1]))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        #self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
