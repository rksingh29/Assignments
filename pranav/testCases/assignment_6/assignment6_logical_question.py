
"""
Question 6 : How to automate when you dont find id/3 objects with no id and similar classname

"""
"""
Answer 1:
"""
#we can use find elements to find all the elements with same class name
elements = webdriver.find_elements_by_classname("classname")

#then iterate through each element to match with the element we want

for element in elements:
    if element.get_text == "test":
        print ("element found")
    else:
        print ("element is not in the list)



Answer 2 :
#we can use absolute xpath feature to find the element

element = webdriver.find_element_by_xpath("absolute_xpath of the element")


if element.get_text() == 'test':
    print("fetched the required element")
    
    
    
    
    
Answer 3:
#we can use sikuli screen class to locate the element

 Screen s = new Screen();
        Pattern openButton = new Pattern(button_name");
        
        
 s.wait(openButton, 20);
        s.click(openButton);
        
        
        
        




