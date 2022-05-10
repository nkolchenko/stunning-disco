# count how many times each word is used in particular string.

#lipsum generator: https://www.lipsum.com/
# lipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing. Praesent eget velit tortor. Ut consectetur magna ultricies."

lipsum = """Amazon EKS runs a single tenant Kubernetes control plane for each cluster. The control plane infrastructure 
isn't shared across clusters or AWS accounts. The control plane consists of at least two API server instances and three 
etcd instances that run across three Availability Zones within an AWS Region. Amazon EKS"""

my_dict = {}
my_incr = 0

my_lipsum = lipsum.replace(",", "").replace(".", "").lower()  # getting rid of commas, dots and lowering case.

my_list = my_lipsum.split(" ")

print("Words Total: ", len(my_list))
while my_incr < len(my_list):

    for element in my_list:
        cnt = my_list.count(my_list[my_incr])
        #print("word", my_incr + 1, " : ", my_list[my_incr], " found ", cnt, " times")

        my_dict.update({my_list[my_incr]: cnt})
        my_incr = my_incr + 1

print(my_dict)
my_dict.
