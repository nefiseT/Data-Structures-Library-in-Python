import math
import hashlib
import random

#-----dİVİSİON METHOD----

def division_hash(key, table_size):
    return hash(key) % table_size

#-----multiplication method

def multiplication_hash(key, table_size):
    h = hash(key)
    square = h*h
    mid = (square >> 16 ) & 0xFFFFFFFF
    return mid % table_size

#------folding method
def folding_hash(key, table_size):
    h = abs(hash(key))
    result = 0

    while h > 0:
        result += h%1000
        h //= 1000
    
    return result % table_size

#------crcytographic hashing (sha256)
def crypto_hash (key, table_size):
    digest = hashlib.sha256(str(key).encode()).hexdigest()
    return int(digest, 16) % table_size



#--------universal hashin g----

class UniversalHash:
    def __init__(self, p=109345121):
        self.p = p
        self.a = random.randint(1, p-1)
        self.b = random.randint(0, p-1)

    def hash(self, key, table_size):
        return ((self.a*hash(key)+ self.b) % self.p) % table_size