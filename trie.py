class Trie:
   def __init__(self):
       self.record=dict()
       self.endofword=False

   def startswith(self,word):
       cur=self
       for c in word:
          if c not in cur.record:
             return False
          cur=cur.record[c]
       return True
       

   def insert(self,word):
       cur=self
       for c in word:
          if c not in cur.record:
             cur.record[c]=Trie()
          cur=cur.record[c]
       cur.endofword=True

   def search(self,word):
       cur=self
       for c in word:
          if c not in cur.record:
             return False
          cur=cur.record[c]
       return cur.endofword

if __name__=="__main__":
   trie=Trie()
   trie.insert("apple")
   trie.insert("mango")
   print(trie.__dict__)
   print(trie.search("apple"))
   print(trie.search("mango"))
   print(trie.startswith("app"))
       
            
     