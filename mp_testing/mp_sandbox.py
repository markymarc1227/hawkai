# from multiprocessing import Queue, Process
# #queues_dict={}


# def random_function(queues,x):
#     for i in range(4):
#         queues[i].put(str(queues[i])+": "+str(x))


# if __name__ == '__main__':

#     video_frames = {
#             0: "video_frame_0",
#             1: "video_frame_1",
#             2: "video_frame_2",
#             3: "video_frame_3"
#         }
#     queues = [Queue() for _ in video_frames]

#     p = Process(target=random_function, args=(queues,1))
#     p.start()

#     p1 = Process(target=random_function, args=(queues,2))
#     p1.start()

#     p2 = Process(target=random_function, args=(queues,3))
#     p2.start()
    
#     print(queues)

#     for i in range(4):
#         x = queues[i].get()
#         x = queues[i].get()
#         print(x)

sample = []

sample[2] = "Sample"
print(sample)
