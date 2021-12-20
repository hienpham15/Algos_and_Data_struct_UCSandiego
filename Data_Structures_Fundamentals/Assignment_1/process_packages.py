#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:24:54 2021

@author: hienpham
"""

from collections import namedtuple, deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        
        self.buffer_list = deque()

    def process(self, request):
        # write your code here
        if len(self.buffer_list) == self.size:
            
            if self.finish_time[0] > request.arrived_at:
                return Response(True, -1)
            
            else:
                if self.finish_time[-1] >= request.arrived_at:
                    start_proc_time = self.finish_time[-1]
                else:
                    start_proc_time = request.arrived_at
                self.buffer_list.popleft()
                self.finish_time.pop(0)
                
                self.buffer_list.append(request)
                self.finish_time.append(start_proc_time + request.time_to_process)
                return Response(False, start_proc_time)
            
        else:
            self.buffer_list.append(request)
            #processing = self.buffer_list[0]
            
            if not self.finish_time:
                request_fin_time = request.time_to_process
                start_request_time = request.arrived_at
            else:
                request_fin_time = self.finish_time[-1] + request.time_to_process
                if self.finish_time[-1] >= request.arrived_at:
                    start_request_time = self.finish_time[-1]
                else:
                    start_request_time = request.arrived_at
                #self.buffer_list.popleft()
                
                if request.arrived_at >=  self.finish_time[0]:
                    self.buffer_list.popleft()
                    self.finish_time.pop(0)
                
            self.finish_time.append(request_fin_time)
            
            return Response(False, start_request_time)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses

buffer = Buffer(3)
n_requests = 6
#requests = [Request(0, 1), Request(1, 1)]
requests = [Request(0, 2), Request(1, 2), Request(2, 2), \
            Request(3, 2), Request(4, 2), Request(5, 2)]

responses = process_requests(requests, buffer)

def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
