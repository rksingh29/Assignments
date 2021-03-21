
"""
Question 6 : How to automate when you dont find id/3 objects with no id and similar classname

"""
"""
Answer :
"""
#we can use find elements to find all the elements with same class name
elements = webdriver.find_elements_by_classname("classname")

#then iterate through each element to match with the element we want

for element in elements:
    if element.get_text == "test":
        print ("elemnt found")
    else:
        print ("element is not in the list)





