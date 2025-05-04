def selection_sort(arr):
    n=len(arr)
    for i in range (n):
        min_index=i
        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
l=int(input('Enter the length of array:'))
arr=[]
print('Enter elements:')
for i in range(l):
    a=int(input('->'))
    arr.append(a)
print('Array:',arr)
sorted=selection_sort(arr)
print('Sorted array:',sorted)

def job_schedule():
    jobs=[]
    n=int(input('Enter the number of jobs:'))
    print('Enter each job in format: JobID Deadline Profit (eg: A 2 100)')
    for _ in range (n):
        job_input=('Enter job details: ').split()
        job_id=job_input[0]
        deadline=job_input[1]
        profit=job_input[2]
        jobs.append((job_id,deadline,profit))
        
    jobs.sort(key=lambda x:x[2],reverse=True)
    max_deadline=max(job[1] for job in jobs)
    slots=[None]*max_deadline
    schedule=[]
    
    for job in jobs:
        job_id,deadline,profit=job
        for i in range(deadline-1,-1,-1):
            if slots[i] is None:
                slots[i]=job_id
                schedule.append(job_id)
                break
    print("Scheduled jobs:",schedule)
job_schedule()