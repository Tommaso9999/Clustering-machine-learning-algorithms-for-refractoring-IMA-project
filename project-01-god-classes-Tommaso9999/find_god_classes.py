import os
import pandas as pd
import javalang



srcPath = r"C:\Users\tomma\OneDrive\Desktop\project-01-god-classes-Tommaso9999\resources\xerces2-j-src"


data = pd.DataFrame(columns=['class_name', 'method_num'])


#Loop trhough files in xerces2-j-src and read source code of java files, then create AST tree. Finally populate dataframe with class names and
#number of methods. 

for path, dirs, files in os.walk(srcPath):
    for file in files:
        if file.endswith('.java'):
            with open(os.path.join(path, file), 'r') as f:
                source_code = f.read()

            
            tree = javalang.parse.parse(source_code)

            class_data = []
            for _, node in tree:
                if isinstance(node, javalang.tree.ClassDeclaration):
                    method_count = len(node.methods)
                    class_name = node.name
                    class_data.append({'class_name': class_name, 'method_num': method_count})

            data = pd.concat([data, pd.DataFrame(class_data)], ignore_index=True)



    

#IDENTIFY GOD CLASSES

#We spot god classes using the mean number of methods + 6sigma. Only classes that have a number of methods above this threshold will be classified 
# as god classes. Names of the god classes and number of methods will then be printed. 

mean= data['method_num'].mean()
SixSigma = (data['method_num'].std()*6)
threshold =  mean+SixSigma

GodClasses=[]


for path, dirs, files in os.walk(srcPath):
    for file in files:
        if file.endswith('.java'):
            with open(os.path.join(path, file), 'r') as f:
                source_code = f.read()

            
            tree = javalang.parse.parse(source_code)

            for _, node in tree:
                if isinstance(node, javalang.tree.ClassDeclaration):
                   
                    Nmethods = len(node.methods)

                  
                    if Nmethods > threshold:

                        GodClasses.append(node.name)

                        print(f'{node.name}  is a God Class with {Nmethods} methods')
                        

