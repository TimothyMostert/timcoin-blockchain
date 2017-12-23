import hashlib as hasher
import datetime as date
import sys

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        selfHash = hasher.sha256()
        selfHash.update(str(self.index) +
                        str(self.timestamp) +
                        str(self.data) +
                        str(self.previous_hash))
        return selfHash.hexdigest()

def create_genesis_block():
        return Block(0,date.datetime.now(), "Genesis Block", "0")

def next_block(last_block, block_entry):
        this_index = last_block.index + 1
        this_timestamp = date.datetime.now()
        this_data = block_entry
        this_hash = last_block.hash
        return Block(this_index, this_timestamp, this_data, this_hash)

def main():

    timchain = [create_genesis_block()]
    previous_block = timchain[0]
    input_data = [""]

    print ("\nWelcome to timcoin v1.0, a blockchain made to keep data safe!\n")
    while ((input_data[0]) != "exit"):
        input_data = raw_input("----| Use the following commands to access this terminal |----\n1. add 'x': To add a message to the blockchain where x is your message to encrypt\n2. display: print the current block chain and its contents to screen\n3. exit: to leave the terminal\n").split()
        if input_data[0] == "add":
            block_entry = " ".join(input_data[1:])
            block_to_add = next_block(previous_block, block_entry)
            timchain.append(block_to_add)
            previous_block = block_to_add
            print "\nSuccessfully Added Block #{} to the timchain!".format(block_to_add.index)
            print "Data added: {}".format(block_entry)
            print "Encrypted Information: {}\n".format(block_to_add.hash)
        elif input_data[0] == "display":
            print "Printing the current encrypted chain:"
            for block in timchain:
                print "Block #{}".format(block.index)
                print "Encrypted Information: {}\n".format(block.hash)
            print "Use private access key to retrieve data\n"

if __name__ == "__main__":
    main()
