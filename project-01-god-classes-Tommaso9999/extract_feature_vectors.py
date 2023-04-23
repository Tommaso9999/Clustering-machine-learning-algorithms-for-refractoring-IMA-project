import os 
import javalang
import pandas as pd


#After running the script find_god_classes.py I could declare a list with their names and from that and xerces2 directory
#I could perform the extraction of feature vecotrs for every god class. 

God_Classes=['CoreDocumentImpl', 'DTDGrammar', 'XSDHandler', 'XIncludeHandler']
srcPath = r"C:\Users\tomma\OneDrive\Desktop\project-01-god-classes-Tommaso9999\resources\xerces2-j-src"
paths =[]
class_list = []



for subdir, dirs, files in os.walk(srcPath):
    for file in files:
        if file.endswith('.java'):
            class_name = file[:-5]  # Takes only java files and removes .java extension

        
            if class_name in God_Classes:
                class_path = os.path.join(subdir, file)
                paths.append(class_path)


for class_path in paths:
    with open(class_path, "r") as f:
        class_source = f.read()
    try:
        java_class = javalang.parse.parse(class_source)
        class_list.append(java_class)
    except javalang.parser.JavaSyntaxError:
       
        pass


#now we can get information about god classes. We do that by creating 4 utility functions. 


#1 FUNCTION THAT RETURNS FIELDS OF A CLASS + LOOP TO POPULATE "fields" VARIABLE WITH VALUES FROM GOD CLASSES. 

def get_fields(java_class):
    fields =set()
    for _, node in java_class.filter(javalang.tree.FieldDeclaration):
        for declarator in node.declarators:
            fields.add(declarator.name)
    return fields


#2 FUNCTION THAT RETURNS METHODS OF A CLASS 

def get_methods(java_class):
    methods = set()
    for _, node in java_class.filter(javalang.tree.MethodDeclaration):
        methods.add(node)
    return methods

#3 FUNCTION THAT RETURNS FIELDS ACCESSED BY A METHOD 

def get_fields_accessed_by_method(method):
    fieldsM = set()   
    for _, node in method.filter(javalang.tree.MemberReference):
        
        if node.qualifier !="": 
            fieldsM.add(node.qualifier)
        else:
            fieldsM.add(node.member)
    return fieldsM

#4 FUNCTION THAT RETURNS METHODS ACCESSED BY A METHOD 

def get_methods_accessed_by_method(method):
    methodsM = set() 
    for _, node in method.filter(javalang.tree.MethodInvocation):

         methodsM.add(node.member)
    return methodsM


# FINAL SECTION THAT CREATES 4 DATAFRAMEs AND  4 CSVs, ONE FOR EVERY CLASS. 
# FOR EVERY METHOD IN GOD CLASSES WE GET A FEATURE VECTOR F THAT CONTAINS FIELD ACCESS AND METHOD INVOKES

results1 = []
results2 = []
results3 = []
results4 = []

folder_name = 'feature_vectors_csv_files'

if not os.path.exists(folder_name):
 os.mkdir(folder_name)


methodsList1 = get_methods(class_list[0])
methodsList11 = {node.name for node in methodsList1}
fieldsList1 = get_fields(class_list[0])

for m in methodsList1:
     accessed_fields = get_fields_accessed_by_method(m)
     accessed_methods = get_methods_accessed_by_method(m)

   

   
     result = {'method_name': m.name}
     for f in accessed_fields:
        if f in fieldsList1:
             result[f] = 1
        
     for i in accessed_methods:
        if i in methodsList11:
             result[i] =1
     
     results1.append(result)


df1 = pd.DataFrame(results1)
df1 = df1.fillna(0)
df1.iloc[:, 1:] =df1.iloc[:, 1:].astype(int)
df1 = df1.drop(df1.columns[(df1 == 0).all()], axis=1)
df1 = df1.drop_duplicates(subset=['method_name'])
df1.to_csv(os.path.join(folder_name, "CoreDocumentImpl.csv"))

print("CoreDocumentImpL","\n",df1.shape)





methodsList2 = get_methods(class_list[1])
methodsList22 = {node.name for node in methodsList2}
fieldsList2 = get_fields(class_list[1])

for m in methodsList2:
        accessed_fields = get_fields_accessed_by_method(m)
        accessed_methods = get_methods_accessed_by_method(m)

        result = {'method_name': m.name}
        for f in accessed_fields:
          if f in fieldsList2:
            result[f] = 1
                
        for i in accessed_methods:
          if i in methodsList22:
            result[i] =1

        results2.append(result)

df2 = pd.DataFrame(results2)
df2 = df2.fillna(0)

df2.iloc[:, 1:] =df2.iloc[:, 1:].astype(int)

df2 = df2.drop(df2.columns[(df2 == 0).all()], axis=1)
df2.drop_duplicates(subset=['method_name'], inplace=True)
df2 = df2.drop_duplicates(subset=['method_name'])
df2.to_csv(os.path.join(folder_name, "DTDGrammar.csv"))


print("DTDGrammar","\n",df2.shape,"\n")



methodsList3 = get_methods(class_list[2])
methodsList33 = {node.name for node in methodsList3}
fieldsList3 = get_fields(class_list[2])


for m in methodsList3:
        
        accessed_fields = get_fields_accessed_by_method(m)
        accessed_methods = get_methods_accessed_by_method(m)          
        result = {'method_name': m.name}

        for f in accessed_fields:
         if f in fieldsList3:
            result[f] = 1

        for i in accessed_methods:
         if i in methodsList33:
            result[i] =1
        
        results3.append(result)
    
        

df3 = pd.DataFrame(results3)
df3 = df3.fillna(0)
df3.iloc[:, 1:] =df3.iloc[:, 1:].astype(int)

df3 = df3.drop(df3.columns[(df3 == 0).all()], axis=1)
df3.drop_duplicates(subset=['method_name'], inplace=True)
df3 = df3.drop_duplicates(subset=['method_name'])
df3.to_csv(os.path.join(folder_name, "XSDHandler.csv"))

print("XSDHandler","\n",df3.shape,"\n")


methodsList4 = get_methods(class_list[3])
methodsList44 = {node.name for node in methodsList4}
fieldsList4 = get_fields(class_list[3])


for m in methodsList4:
        accessed_fields = get_fields_accessed_by_method(m)
        accessed_methods = get_methods_accessed_by_method(m)
        result = {'method_name': m.name}
        for f in accessed_fields:
          if f in fieldsList4:
            result[f] = 1
        
        for i in accessed_methods:
         if i in methodsList44:
            result[i] =1

        results4.append(result)

df4 = pd.DataFrame(results4)
df4 = df4.fillna(0)
df4.iloc[:, 1:] =df4.iloc[:, 1:].astype(int)
df4 = df4.drop(df4.columns[(df4 == 0).all()], axis=1)


df4.drop_duplicates(subset=['method_name'], inplace=True)
df4 = df4.drop_duplicates(subset=['method_name'])
df4.to_csv(os.path.join(folder_name, "XIncludeHandler.csv"))


print("XIncludeHandler","\n",df4.shape)






