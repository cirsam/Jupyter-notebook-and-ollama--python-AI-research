import re

class simpletokenizer:
        def __init__(self,text):
            print(text)
            self.ids = []
            self.words = []
            self.text=text
        def encode(self):
            
            
              
            my_list = re.split(r'\s+', self.text)
            for index, value in enumerate(my_list):
                print(f"Index: {index}, Value: {value}")
                self.ids.append(index)
                self.words. append(value)
                #print(sorted(set(words)))
                
            print("\nthe words\n",set(self.words))    
            return self.ids
            
        
    
        def decode(self):
            my_list = re.split(r'\s+', self.text)
            mywords=self.words
            for i, id in enumerate(self.ids):
             print(f"mylist[{id}]",self.words[id])
                
            print("\n the decoded text is\n"," ".join(self.words))


                
text="this is a test. in the text."
tokenizer=simpletokenizer(text)
tokens=tokenizer.encode()
print("ids", tokens)
tokenizer.decode()
