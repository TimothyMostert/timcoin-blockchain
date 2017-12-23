timchain = [create_genesis_block()]
previous_block = timchain[0]

num_of_blocks = 20

for i in range(0, num_of_blocks):
    block_to_add = next_block(previous_block)
    timchain.append(block_to_add)
    previous_block = block_to_add

    print "Block #{} has been added to the timchain!".format(block_to_add.index)
    print "Hashed Element: {}\n".format(block_to_add.hash)
